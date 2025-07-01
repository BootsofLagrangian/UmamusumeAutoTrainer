<template>
  <div id="create-task-list-modal" class="modal fade">
    <div  class="modal-dialog modal-dialog-centered modal-xl">
      <div class="modal-content">
        <h5 class="modal-header">
          새 작업 생성
        </h5>
        <div class="modal-body">
          <form>
            <div class="form-group">
              <label for="selectTaskType">⭐ 작업 선택</label>
              <select v-model="selectedUmamusumeTaskType" class="form-control" id="selectTaskType">
                <option v-for="task in umamusumeTaskTypeList" :value="task">{{task.name}}</option>
              </select>
            </div>
            <div class="form-group">
              <label for="selectExecuteMode">⭐ 실행 모드 선택</label>
              <select v-model="selectedExecuteMode" class="form-control" id="selectExecuteMode">
                <option value=1>1회성</option>
              </select>
            </div>
            <div class="row">
              <div class="col">
                <div class="form-group">
                  <label for="selectSernaio">⭐ 시나리오 선택</label>
                  <select class="form-control" id="selectSernaio">
                    <option value=1>URA</option>
                  </select>
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="selectUmamusume">우마무스메 선택</label>
                  <select disabled class="form-control" id="selectUmamusume">
                    <option value=1>이전 선택 사용</option>
                  </select>
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="selectAutoRecoverTP">체력 부족 시 자동 회복 (물약만 사용)</label>
                  <select v-model="recoverTP" class="form-control" id="selectAutoRecoverTP">
                    <option :value=true>예</option>
                    <option :value=false>아니오</option>
                  </select>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-8">
                <div class="form-group">
                  <label for="race-select">⭐ 프리셋 사용</label>
                    <div class="form-inline">
                      <select v-model="presetsUse" style="text-overflow: ellipsis;width: 40em;"  class="form-control" id="use_presets">
                        <option v-for="set in cultivatePresets" :value="set">{{set.name}}</option>
                      </select>
                      <span class="btn auto-btn ml-2" v-on:click="applyPresetRace">적용</span>
                    </div>
                </div>
              </div>
              <div class="col-4">
                <div class="form-group">
                  <label for="presetNameEditInput">프리셋으로 저장</label>
                  <div class="form-inline">
                    <input v-model="presetNameEdit" type="text" class="form-control" id="presetNameEditInput" placeholder="프리셋 이름">
                    <span class="btn auto-btn ml-2" v-on:click="addPresets">저장</span>
                  </div>
                </div>
              </div>
            </div>
            
            <div class="row">
              <div class="col-4">
                <div class="form-group">
                  <label>⭐ 서포트 카드 선택</label>
                  <select v-model="selectedSupportCard" class="form-control" id="selectedSupportCard">
                    <option v-for="card in umausumeSupportCardList" :value="card">({{card.desc}}) {{card.name}}</option>
                  </select>
                </div>
              </div>
              <div class="col-2">
                <div class="form-group">
                  <label for="selectSupportCardLevel">서포트 카드 레벨 (≥)</label>
                  <input v-model="supportCardLevel" type="number" class="form-control" id="selectSupportCardLevel" placeholder="">
                </div>
              </div>
              <div class="col-3">
                <div class="form-group">
                  <label for="inputClockUseLimit">시계 사용 제한</label>
                  <input v-model="clockUseLimit" type="number" class="form-control" id="inputClockUseLimit" placeholder="">
                </div>
              </div>
            </div>
            <div class="form-group">
              <div>⭐ 목표 스테이터스 (값이 확실하지 않으면 수동으로 한 번 플레이해서 최종 수치 입력)</div>
            </div>
            <div class="row">
              <div class="col">
                <div class="form-group">
                    <label for="speed-value-input">스피드</label>
                    <input type="number" v-model="expectSpeedValue" class="form-control" id="speed-value-input">
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="stamina-value-input">스태미나</label>
                  <input type="number" v-model="expectStaminaValue" class="form-control" id="stamina-value-input">
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="power-value-input">파워</label>
                  <input type="number" v-model="expectPowerValue" class="form-control" id="power-value-input">
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="will-value-input">근성</label>
                  <input type="number" v-model="expectWillValue" class="form-control" id="will-value-input">
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="intelligence-value-input">지능</label>
                  <input type="number" v-model="expectIntelligenceValue" class="form-control" id="intelligence-value-input">
                </div>
              </div>
            </div>
            <div>
              <div class="form-group">
              <span v-if="!showAdvanceOption" class="btn auto-btn" style="width: 100%; background-color:#6c757d;" v-on:click="switchAdvanceOption">고급 옵션 펼치기</span>
              <span v-if="showAdvanceOption" class="btn auto-btn" style="width: 100%; background-color:#6c757d;" v-on:click="switchAdvanceOption">고급 옵션 접기</span>
              </div>
            </div>
            <div v-if ="showAdvanceOption">
              <div class="form-group">
                <div>⭐ 추가 가중치</div>
              </div>
              <p>최종 목표 스테이터스에 영향을 주지 않고 AI 트레이닝 선호도를 조정합니다. 특정 트레이닝 유형을 우선시하는 데 사용됩니다. 권장 가중치 범위 [-1.0 ~ 1.0], 0은 추가 가중치 없음을 의미합니다.</p>
              <p>서포트 카드나 종마가 약할 때, 한 속성의 가중치를 늘리는 동시에 다른 속성들을 같은 양만큼 줄이세요.</p>
              <div style="margin-bottom: 10px;">1학년</div>
              <div class="row">
                <div v-for="v,i in extraWeight1" class="col">
                  <div class="form-group">
                      <input type="number" v-model="extraWeight1[i]" class="form-control" id="speed-value-input">
                  </div>
                </div>
              </div>
              <div style="margin-bottom: 10px;">2학년</div>
              <div class="row">
                <div v-for="v,i in extraWeight2" class="col">
                  <div class="form-group">
                      <input type="number" v-model="extraWeight2[i]" class="form-control" id="speed-value-input">
                  </div>
                </div>
              </div>
              <div style="margin-bottom: 10px;">3학년</div>
              <div class="row">
                <div v-for="v,i in extraWeight3" class="col">
                  <div class="form-group">
                      <input type="number" v-model="extraWeight3[i]" class="form-control" id="speed-value-input">
                  </div>
                </div>
              </div>
            </div>

            <div class="form-group">
              <div>⭐ 레이싱 전략 선택</div>
            </div>
            <div class="row">
              <div class="col">
                <div class="form-group">
                  <label for="selectTactic1">1학년</label>
                  <select v-model="selectedRaceTactic1" class="form-control" id="selectTactic1">
                    <option :value=1>후방추입 (오이코미)</option>
                    <option :value=2>선입 (사시)</option>
                    <option :value=3>선행 (센코)</option>
                    <option :value=4>도주 (니게)</option>
                  </select>
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="selectTactic2">2학년</label>
                  <select v-model="selectedRaceTactic2" class="form-control" id="selectTactic2">
                    <option :value=1>후방추입 (오이코미)</option>
                    <option :value=2>선입 (사시)</option>
                    <option :value=3>선행 (센코)</option>
                    <option :value=4>도주 (니게)</option>
                  </select>
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label for="selectTactic3">3학년</label>
                  <select v-model="selectedRaceTactic3" class="form-control" id="selectTactic3">
                    <option :value=1>후방추입 (오이코미)</option>
                    <option :value=2>선입 (사시)</option>
                    <option :value=3>선행 (센코)</option>
                    <option :value=4>도주 (니게)</option>
                  </select>
                </div>
              </div>
            </div>
            <div class="form-group">
              <div class="row">
                <div class="col">
                  <div class="form-group">
                    <label for="race-select">⭐ 추가 레이스 선택</label>
                    <textarea type="text" disabled v-model="extraRace" class="form-control" id="race-select"></textarea>
                  </div>
                </div>
              </div>
              <div class="form-group">
              <span v-if="!showRaceList" class="btn auto-btn" style="width: 100%; background-color:#6c757d;" v-on:click="switchRaceList">레이스 옵션 펼치기</span>
              <span v-if="showRaceList" class="btn auto-btn" style="width: 100%; background-color:#6c757d;" v-on:click="switchRaceList">레이스 옵션 접기</span>
              </div>
              <div class="row" v-if="showRaceList"> 
                <div class="col">
                  <div>1학년</div>
                  <br/>
                  <div class="form-check">
                    <div v-for="race in umamusumeRaceList_1">
                      <input class="form-check-input position-static" v-model="extraRace" type="checkbox" :id="race.id" :value="race.id"><label :for="race.id" v-if="race.type==='GI'||race.type==='GII'&&!this.hideG2||race.type==='GIII'&&!this.hideG3">
                        <span v-if="race.type === 'GIII'">&nbsp;<span style="background-color: #58C471;" class="badge badge-pill badge-secondary">{{race.type}}</span>&nbsp;</span>
                        <span v-if="race.type === 'GII'">&nbsp;<span style="background-color: #F75A86;" class="badge badge-pill badge-secondary">{{race.type}}</span>&nbsp;</span>
                        <span v-if="race.type === 'GI'">&nbsp;<span style="background-color: #3485E3;" class="badge badge-pill badge-secondary">{{race.type}}</span>&nbsp;</span>{{race.date}} {{race.name}}</label>
                    </div>
                  </div>
                </div>
                <div class="col">
                  <div>2학년</div>
                  <br/>
                  <div class="form-check">
                    <div v-for="race in umamusumeRaceList_2">
                      <input class="form-check-input position-static" v-model="extraRace" type="checkbox" :id="race.id" :value="race.id"><label :for="race.id" v-if="race.type==='GI'||race.type==='GII'&&!this.hideG2||race.type==='GIII'&&!this.hideG3">
                        <span v-if="race.type === 'GIII'">&nbsp;<span style="background-color: #58C471;" class="badge badge-pill badge-secondary">{{race.type}}</span>&nbsp;</span>
                        <span v-if="race.type === 'GII'">&nbsp;<span style="background-color: #F75A86;" class="badge badge-pill badge-secondary">{{race.type}}</span>&nbsp;</span>
                        <span v-if="race.type === 'GI'">&nbsp;<span style="background-color: #3485E3;" class="badge badge-pill badge-secondary">{{race.type}}</span>&nbsp;</span>{{race.date}} {{race.name}}</label>
                    </div>
                  </div>
                </div>
                <div class="col">
                  <div>3학년</div>
                  <br/>
                  <div class="form-check">
                    <div v-for="race in umamusumeRaceList_3">
                      <input class="form-check-input position-static" v-model="extraRace" type="checkbox" :id="race.id" :value="race.id"><label :for="race.id" v-if="race.type==='GI'||race.type==='GII'&&!this.hideG2||race.type==='GIII'&&!this.hideG3">
                        <span v-if="race.type === 'GIII'">&nbsp;<span style="background-color: #58C471;" class="badge badge-pill badge-secondary">{{race.type}}</span>&nbsp;</span>
                        <span v-if="race.type === 'GII'">&nbsp;<span style="background-color: #F75A86;" class="badge badge-pill badge-secondary">{{race.type}}</span>&nbsp;</span>
                        <span v-if="race.type === 'GI'">&nbsp;<span style="background-color: #3485E3;" class="badge badge-pill badge-secondary">{{race.type}}</span>&nbsp;</span>{{race.date}} {{race.name}}</label>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="form-group mb-0">
              <div class="row">
                <div class="col">
                  <div class="form-group">
                    <label for="skill-learn">⭐ 스킬 학습</label>
                  </div>
                </div>
              </div>
            </div>
            <div v-for="(item,index) in skillLearnPriorityList" :key="item.priority">
              <div class="form-group row">
                <label class="col-sm-3" for="'skill-learn-' + item.id">❗ 학습 우선순위 {{ item.priority+1 }}</label>
                <div class="col-sm-6">
                  <textarea type="text"  v-model="item.skills" class="form-control" id="skill-learn-priority" placeholder="Skill1 name, Skill2 name,... (use English comma)"></textarea>
                </div>
                <div class="col-sm-3">
                  <span class="red-button auto-btn ml-2" v-on:click="deleteBox(item,index)">현재 우선순위 삭제</span>
                </div>
              </div>
            </div>
            <span class="btn auto-btn ml-2" v-on:click="addBox(item)">우선순위 추가</span>
            <div class="form-group mb-0">
              <div class="row">
                <div class="col">
                  <div class="form-group">
                    <br>
                    <label for="skill-learn-default">✅ (All other unlisted skills are at this priority)</label>
                  </div>
                </div>
              </div>
            </div>

            <div class="form-group mb-0">
              <div class="row">
                <div class="col">
                  <div class="form-group">
                    <label for="skill-learn-blacklist">⛔ 블랙리스트 (어떤 상황에서도 이 스킬들을 학습하지 않음)</label>
                    <textarea type="text"  v-model="skillLearnBlacklist" class="form-control" id="skill-learn-blacklist" placeholder="Iron Will, Swift as Wind,... (surely no one would pick these)"></textarea>
                  </div>
                </div>
              </div>
            </div>
            

            <div class="form-group">
              <div class="row">
                <div class="col-3">
                  <div class="form-group">
                    <label for="learnSkillOnlyUserProvidedSelector">Only allow learning skills listed above during training</label>
                    <select v-model="learnSkillOnlyUserProvided" class="form-control" id="learnSkillOnlyUserProvidedSelector">
                      <option :value=true>Yes</option>
                      <option :value=false>No</option>
                    </select>
                  </div>
                </div>
                <div class="col-3">
                  <div class="form-group">
                    <label for="learnSkillBeforeRaceSelector">Learn skills before races</label>
                    <select disabled v-model="learnSkillBeforeRace" class="form-control" id="learnSkillBeforeRace">
                      <option :value=true>Yes</option>
                      <option :value=false>No</option>
                    </select>
                  </div>
                </div>
                <div class="col-3">
                  <div class="form-group">
                    <label for="inputSkillLearnThresholdLimit">Learn skills when points exceed this value during training</label>
                    <input v-model="learnSkillThreshold" type="number" class="form-control" id="inputSkillLearnThresholdLimit" placeholder="">
                  </div>
                </div>
              </div>
            </div>
          </form>
          <!-- <div class="part">
            <br>
            <h6>定时设置</h6>
            <hr />
            <div class="row">
              <label for="cronInput" class="col-2 col-form-label">cron表达式</label>
              <div class="col-10">
                <input v-model="cron"  class="form-control" id="cronInput">
              </div>
            </div>
          </div> -->
        </div>
        <div class="modal-footer">
          <span class="btn auto-btn" v-on:click="addTask">확인</span>
        </div>
      </div>
      <!-- 通知 -->
      <div class="position-fixed" style="z-index: 5; right: 40%; width: 300px;">
        <div id="liveToast" class="toast hide" role="alert" aria-live="assertive" aria-atomic="true" data-delay="2000">
          <div class="toast-body">
            ✔ 프리셋 저장 완료
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TaskEditModal",
  data:function () {
    return{
      showAdvanceOption:false,
      showRaceList:false,
      dataReady:false,
      hideG2: false,
      hideG3: false,
      levelDataList:[],
      umamusumeTaskTypeList:[
        {
          id: 1,
          name: "Training",
        }
      ],
      umamusumeList:[
        {id:1, name:'Special Week'},
        {id:2, name:'Silent Suzuka'},
        {id:3, name:'Tokai Teio'},
        {id:4, name:'Maruzensky'},
        {id:5, name:'Oguri Cap'},
        {id:6, name:'Gold Ship'},
        {id:7, name:'Mejiro McQueen'},
        {id:8, name:'Opera O'},
        {id:9, name:'Rudolf Symbol'},
        {id:10, name:'Rice Shower'},
        {id:11, name:'Gold Ship'},
        {id:12, name:'Vodka'},
        {id:13, name:'Daiwa Scarlet'},
        {id:14, name:'Grass Wonder'},
        {id:15, name:'El Condor Pasa'},
        {id:16, name:'T.M. Opera O'},
        {id:17, name:'Narita Brian'},
        {id:18, name:'Super Creek'},
        {id:19, name:'Mejiro Ryan'},
        {id:20, name:'Agnes Tachyon'},
        {id:21, name:'Winning Ticket'},
        {id:22, name:'Sakura Bakushin O'},
        {id:23, name:'Haru Urara'},
        {id:24, name:'Taiki Shuttle'},
        {id:25, name:'Fine Motion'},
        {id:26, name:'Biwa Hayahide'},
      ],
      umausumeSupportCardList:[
        {id:1, name:'Beyond the Brilliant Scene', desc:'Speed Suzuka'},
        {id:2, name:'Presenting the Best Performance in Japan', desc: 'Guts Special Week'},
        {id:3, name:'If You Have Dreams, Shout Them Loud!', desc: 'Speed Teio'},
        {id:4, name:'Unsinkable Assault', desc: 'Stamina Gold Ship'},
        {id:5, name:'The Vodka Way', desc: 'Power Vodka'},
        {id:6, name:'Standing Out Among All the Colors', desc: 'Guts Grass Wonder'},
        {id:7, name:'Passionate Champion', desc: 'Power El Condor Pasa'},
        {id:8, name:'Long-Awaited Scheme', desc: 'Stamina Seiun Sky'},
        {id:9, name:'Lightning Girl Splitting the Sky!', desc: 'Stamina Tamamo Cross'},
        {id:10, name:'Heartfelt Gratitude', desc: 'Wisdom Mihono Bourbon'},
        {id:11, name:'Run and Shine', desc: 'Guts Fuji Kiseki'},
        {id:12, name:'B·N·Winner!', desc: 'Guts Ticket'},
        {id:13, name:'Forward 7 Centimeters Ahead', desc: 'Wisdom Air Groove'},
        {id:14, name:'Run(my)way', desc: 'Speed King Halo'},
        {id:15, name:'So Fast! So Good! So Fast!', desc: 'Speed Bakushin O'},
        {id:16, name:'A Reassuring Candy', desc: 'Stamina Super Creek'},
        {id:17, name:'This is My Uma Idol Way', desc: 'Power Falcon'},
        {id:18, name:'Even Though Still Growing', desc: 'Speed Nishino Flower'},
        {id:19, name:'Special Move! Twin Carrot Punch', desc: 'Speed Biwa Hayahide'},
        {id:20, name:'Welcome to Tracen Academy!', desc: 'Friend Cap'},
        {id:21, name:'The Sunset is the Color of Yearning', desc: 'Speed Special Week'},
        {id:22, name:'Be Loved by Everyone', desc: 'Power Oguri Cap'},
        {id:23, name:'Turbo Engine Full Power!', desc: 'Speed Twin Turbo'},
        {id:24, name:'The Burning Fire in My Heart Cannot Be Suppressed', desc: 'Power Yaeno Muteki'},
        {id:25, name:'The Heat Wave Behind is My Drive', desc: 'Speed Hokko Tarumae'},
        {id:26, name:'Surpassing That Figure Ahead', desc: 'Stamina Admire Vega'},
        {id:27, name:'As a Bride!', desc: 'Speed Kawakami Princess'},
        {id:28, name:'Enjoying the Cool Alone?', desc: 'Speed Smart Falcon'},
        {id:29, name:'The Burning Fire in My Heart Cannot Be Suppressed', desc: 'Power Yaeno Muteki'},
        {id:30, name:'Even Covered in Mud, Still Chase Dreams', desc: 'Wisdom Narita Top Road'},
        {id:31, name:'Two Pieces', desc: 'Speed Narita Brian'},
        {id:32, name:'Apprentice Witch and the Long Night', desc: 'Speed Smart Falcon'},
      ],
      umamusumeRaceList_1:[
        {id:1401, name:'函馆初级锦标赛',date: '7月后', type: 'GIII'},
        {id:1601, name:'新潟初级锦标赛',date: '8月后', type: 'GIII'},
        {id:1701, name:'札幌初级锦标赛',date: '9月前', type: 'GIII'},
        {id:1702, name:'小仓初级锦标赛',date: '9月前', type: 'GIII'},
        {id:1902, name:'沙漠皇家杯',date: '10月前', type: 'GIII'},
        {id:2002, name:'阿耳忒弥斯锦标赛',date: '10月后', type: 'GIII'},
        {id:2102, name:'京王杯初级锦标赛',date: '11月前', type: 'GII'},
        {id:2103, name:'每日杯初级锦标赛',date: '11月前', type: 'GII'},
        {id:2104, name:'幻想锦标赛',date: '11月前', type: 'GIII'},
        {id:2202, name:'东京体育馆初级锦标赛',date: '11月后', type: 'GIII'},
        {id:2203, name:'京都初级锦标赛',date: '11月后', type: 'GIII'},
        {id:2302, name:'阪神初级少女杯赛', date: '12月前', type: 'GI'},
        {id:2303, name:'朝日杯未来锦标赛', date: '12月前', type: 'GI'},
        {id:2401, name:'希望锦标赛', date: '12月后', type: 'GI'},
      ],
      umamusumeRaceList_2:[
        {id:2501, name:'新山纪念', date: '1月前', type: 'GIII'},
        {id:2502, name:'精灵锦标赛', date: '1月前', type: 'GIII'},
        {id:2503, name:'京成杯', date: '1月前', type: 'GIII'},
        {id:2701, name:'如月奖', date: '2月前', type: 'GIII'},
        {id:2702, name:'女王杯', date: '2月前', type: 'GIII'},
        {id:2703, name:'共同通信杯', date: '2月前', type: 'GIII'},
        {id:2903, name:'弥生奖', date: '3月前', type: 'GII'},
        {id:2904, name:'少女竞技赛', date: '3月前', type: 'GII'},
        {id:2905, name:'郁金香奖', date: '3月前', type: 'GII'},
        {id:3001, name:'百花杯', date: '3月后', type: 'GIII'},
        {id:3003, name:'春季锦标赛', date: '3月后', type: 'GII'},
        {id:3004, name:'游隼锦标赛', date: '3月后', type: 'GIII'},
        {id:3005, name:'每日杯', date: '3月后', type: 'GIII'},
        {id:3103, name:'樱花奖', date: '4月前', type: 'GI'},
        {id:3104, name:'皐月奖', date: '4月前', type: 'GI'},
        {id:3105, name:'无翼鸟杯', date: '4月前', type: 'GII'},
        {id:3106, name:'阿灵顿杯', date: '4月前', type: 'GIII'},
        {id:3204, name:'芙洛拉锦标赛', date: '4月后', type: 'GII'},
        {id:3205, name:'青叶奖', date: '4月后', type: 'GII'},
        {id:3303, name:'广播协会英里杯', date: '5月前', type: 'GI'},
        {id:3304, name:'京都新闻杯', date: '5月前', type: 'GII'},
        {id:3403, name:'奥克斯', date: '5月后', type: 'GI'},
        {id:3404, name:'全国德比 东京优骏', date: '5月后', type: 'GI'},
        {id:3405, name:'葵锦标赛', date: '5月后', type: 'GIII'},
        {id:3504, name:'东京英里赛', date: '6月前', type: 'GI'},
        {id:3506, name:'叶森杯', date: '6月前', type: 'GIII'},
        {id:3505, name:'鸣尾纪念', date: '6月前', type: 'GIII'},
        {id:3501, name:'人鱼锦标赛', date: '6月前', type: 'GIII'},
        {id:3608, name:'函馆短途锦标赛', date: '6月后', type: 'GIII'},
        {id:3601, name:'独角兽锦标赛', date: '6月后', type: 'GIII'},
        {id:3607, name:'宝冢纪念', date: '6月后', type: 'GI'},
        {id:3701, name:'南河三锦标赛', date: '7月前', type: 'GIII'},		
        {id:3708, name:'函馆纪念', date: '7月前', type: 'GIII'},
        {id:3706, name:'中部广播奖', date: '7月前', type: 'GIII'},
        {id:3707, name:'七夕奖', date: '7月前', type: 'GIII'},
        {id:3709, name:'日经广播奖', date: '7月前', type: 'GIII'},
        {id:3705, name:'全国泥地德比', date: '7月前', type: 'GI'},
		{id:3801, name:'皇后锦标赛', date: '7月后', type: 'GIII'},
		{id:3803, name:'中京纪念', date: '7月后', type: 'GIII'},
		{id:3804, name:'朱鹭夏季冲刺赛', date: '7月后', type: 'GIII'},
		{id:3901, name:'榆木锦标赛', date: '8月前', type: 'GIII'},
		{id:3906, name:'小仓纪念', date: '8月前', type: 'GIII'},
		{id:3907, name:'关屋纪念', date: '8月前', type: 'GIII'},
		{id:3908, name:'猎豹锦标赛', date: '8月前', type: 'GIII'},
		{id:4005, name:'札幌纪念', date: '8月后', type: 'GII'},
		{id:4006, name:'北九州纪念', date: '8月后', type: 'GIII'},
		{id:4007, name:'科尼杯', date: '8月后', type: 'GIII'},
        {id:4101, name:'人马锦标赛', date: '9月前', type: 'GII'},
        {id:4102, name:'玫瑰锦标赛', date: '9月前', type: 'GII'},
        {id:4103, name:'新潟記念', date: '9月前', type: 'GIII'},
        {id:4104, name:'京成杯秋季让磅赛', date: '9月前', type: 'GIII'},
        {id:4105, name:'紫苑锦标赛', date: '9月前', type: 'GIII'},
        {id:4201, name:'短途者锦标赛', date: '9月后', type: 'GI'},
        {id:4202, name:'神户新闻杯', date: '9月后', type: 'GII'},
        {id:4203, name:'全国邀请赛', date: '9月后', type: 'GII'},
        {id:4204, name:'圣光纪念', date: '9月后', type: 'GII'},
        {id:4205, name:'天狼星锦标赛', date: '9月后', type: 'GIII'},
        {id:4301, name:'每日王冠', date: '10月前', type: 'GII'},
        {id:4302, name:'京都大奖赛', date: '10月前', type: 'GII'},
        {id:4303, name:'府中优俊少女锦标赛', date: '10月前', type: 'GIII'},
        {id:4401, name:'天鹅锦标赛', date: '10月后', type: 'GII'},
        {id:4402, name:'富士锦标赛', date: '10月后', type: 'GII'},
        {id:4407, name:'天王奖(秋)', date: '10月后', type: 'GI'},
        {id:4408, name:'秋华奖', date: '10月后', type: 'GI'},
        {id:4409, name:'菊花奖', date: '10月后', type: 'GI'},
		{id:4501, name:'白银杯', date: '11月前', type: 'GII'},
		{id:4502, name:'都城锦标赛', date: '11月前', type: 'GIII'},
		{id:4503, name:'武藏野锦标赛', date: '11月前', type: 'GIII'},
		{id:4504, name:'松浪纪念', date: '11月前', type: 'GIII'},
        {id:4506, name:'伊丽莎白女王杯', date: '11月前', type: 'GI'},
        {id:4507, name:'全国育成杯 女士经典赛', date: '11月前', type: 'GI'},
        {id:4508, name:'全国育成杯 短途赛', date: '11月前', type: 'GI'},
        {id:4509, name:'全国育成杯 经典赛', date: '11月前', type: 'GI'},
        {id:4601, name:'京阪杯', date: '11月后', type: 'GIII'},
        {id:4607, name:'英里冠军赛', date: '11月后', type: 'GI'},
        {id:4608, name:'全国杯', date: '11月后', type: 'GI'},
        {id:4701, name:'长途锦标赛', date: '12月前', type: 'GII'},
        {id:4702, name:'挑战杯', date: '12月前', type: 'GIII'},
        {id:4703, name:'中日新闻杯', date: '12月前', type: 'GIII'},
		{id:4704, name:'五车二锦标赛', date: '12月前', type: 'GIII'},
        {id:4705, name:'绿松石锦标赛', date: '12月前', type: 'GIII'},
        {id:4711, name:'全国冠军杯', date: '12月前', type: 'GI'},
		{id:4801, name:'阪神杯', date: '12月后', type: 'GII'},
        {id:4804, name:'中山大奖赛', date: '12月后', type: 'GI'},
        {id:4805, name:'东京大奖赛', date: '12月后', type: 'GI'},
      ],
      umamusumeRaceList_3:[
        {id:4901, name:'日经新春杯', date: '1月前', type: 'GII'},
        {id:4902, name:'京都金杯', date: '1月前', type: 'GIII'},
        {id:4903, name:'中山金杯', date: '1月前', type: 'GIII'},
        {id:4904, name:'爱知杯', date: '1月前', type: 'GIII'},
        {id:5001, name:'东海锦标赛', date: '1月后', type: 'GII'},
        {id:5002, name:'合众国交流杯', date: '1月后', type: 'GII'},
        {id:5003, name:'丝绸之路锦标赛', date: '1月后', type: 'GIII'},
        {id:5004, name:'根岸锦标赛', date: '1月后', type: 'GIII'},
        {id:5101, name:'京都纪念', date: '2月前', type: 'GII'},
        {id:5102, name:'东京新闻杯', date: '2月前', type: 'GIII'},
        {id:5201, name:'中山纪念', date: '2月后', type: 'GII'},
        {id:5202, name:'京都优骏少女锦标赛', date: '2月后', type: 'GIII'},
        {id:5203, name:'钻石锦标赛', date: '2月后', type: 'GIII'},
        {id:5204, name:'小仓大奖赛', date: '2月后', type: 'GIII'},
		{id:5205, name:'阪急杯', date: '2月后', type: 'GIII'},
        {id:5208, name:'二月锦标赛', date: '2月后', type: 'GI'},
        {id:5301, name:'金鯱賞', date: '3月前', type: 'GII'},
        {id:5302, name:'海洋锦标赛', date: '3月前', type: 'GIII'},
        {id:5303, name:'中山优俊少女锦标赛', date: '3月前', type: 'GIII'},
		{id:5401, name:'阪神大奖赛', date: '3月后', type: 'GII'},
		{id:5402, name:'日经奖', date: '3月后', type: 'GII'},
        {id:5403, name:'三月锦标赛', date: '3月后', type: 'GIII'},
        {id:5406, name:'中京短途赛', date: '3月后', type: 'GI'},
        {id:5407, name:'大阪杯', date: '3月后', type: 'GI'},
        {id:5501, name:'阪神优俊少女锦标赛', date: '4月前', type: 'GII'},
		{id:5502, name:'德比伯爵挑战赛', date: '4月前', type: 'GIII'},
        {id:5503, name:'心宿二锦标赛', date: '4月前', type: 'GIII'},
        {id:5601, name:'英里杯', date: '4月后', type: 'GII'},
		{id:5602, name:'松浪优俊少女锦标赛', date: '4月后', type: 'GIII'},
        {id:5605, name:'天王奖(春)', date: '4月后', type: 'GI'},
        {id:5701, name:'京王杯春季杯', date: '5月前', type: 'GII'},
        {id:5702, name:'新潟大奖赛', date: '5月前', type: 'GIII'},
        {id:5709, name:'维多利亚英里杯', date: '5月前', type: 'GI'},
        {id:5801, name:'目黑記念', date: '5月后', type: 'GII'},
        {id:5802, name:'平安锦标赛', date: '5月后', type: 'GIII'},
		{id:5901, name:'人鱼锦标赛', date: '6月前', type: 'GIII'},
        {id:5904, name:'东京英里赛', date: '6月前', type: 'GI'},
        {id:5905, name:'鸣尾纪念', date: '6月前', type: 'GIII'},
		{id:5906, name:'叶森杯', date: '6月前', type: 'GIII'},
        {id:6006, name:'宝冢纪念', date: '6月后', type: 'GI'},
        {id:6007, name:'函館短途锦标赛', date: '6月后', type: 'GIII'},
        {id:6008, name:'帝王奖', date: '6月后', type: 'GI'},
		{id:6101, name:'南河三锦标赛', date: '7月前', type: 'GIII'},
		{id:6105, name:'中部广播奖', date: '7月前', type: 'GIII'},
		{id:6106, name:'七夕奖', date: '7月前', type: 'GIII'},
		{id:6107, name:'函馆纪念', date: '7月前', type: 'GIII'},
		{id:6201, name:'皇后锦标赛', date: '7月后', type: 'GIII'},
		{id:6203, name:'中京纪念', date: '7月后', type: 'GIII'},
		{id:6204, name:'朱鹭夏季冲刺赛', date: '7月后', type: 'GIII'},
		{id:6301, name:'榆木锦标赛', date: '8月前', type: 'GIII'},
		{id:6306, name:'小仓纪念', date: '8月前', type: 'GIII'},
		{id:6307, name:'关屋纪念', date: '8月前', type: 'GIII'},
		{id:6405, name:'札幌纪念', date: '8月后', type: 'GII'},
		{id:6406, name:'北九州纪念', date: '8月后', type: 'GIII'},
		{id:6407, name:'科尼杯', date: '8月后', type: 'GIII'},
        {id:6501, name:'人马锦标赛', date: '9月前', type: 'GII'},
        {id:6502, name:'新潟記念', date: '9月前', type: 'GIII'},
        {id:6503, name:'京成杯秋季让磅赛', date: '9月前', type: 'GIII'},
        {id:6603, name:'天狼星锦标赛', date: '9月后', type: 'GIII'},
        {id:6602, name:'全国邀请赛', date: '9月后', type: 'GII'},
        {id:6601, name:'短途者锦标赛', date: '9月后', type: 'GI'},
        {id:6701, name:'每日王冠', date: '10月前', type: 'GII'},
        {id:6702, name:'京都大奖赛', date: '10月前', type: 'GII'},
		{id:6703, name:'府中优俊少女锦标赛', date: '10月前', type: 'GII'},
        {id:6801, name:'天鹅锦标赛', date: '10月后', type: 'GII'},
        {id:6802, name:'富士锦标赛', date: '10月后', type: 'GII'},
        {id:6807, name:'天王奖(秋)', date: '10月后', type: 'GI'},
        {id:6901, name:'白银杯', date: '11月前', type: 'GII'},
		{id:6902, name:'都城锦标赛', date: '11月前', type: 'GIII'},
		{id:6903, name:'武藏野锦标赛', date: '11月前', type: 'GIII'},
		{id:6904, name:'松浪纪念', date: '11月前', type: 'GIII'},
        {id:6906, name:'伊丽莎白女王杯', date: '11月前', type: 'GI'},
        {id:6907, name:'全国育成杯 女士经典赛', date: '11月前', type: 'GI'},
        {id:6908, name:'全国育成杯 短途赛', date: '11月前', type: 'GI'},
        {id:6909, name:'全国育成杯 经典赛', date: '11月前', type: 'GI'},
        {id:7001, name:'京阪杯', date: '11月后', type: 'GIII'},
        {id:7007, name:'英里冠军赛', date: '11月后', type: 'GI'},
        {id:7008, name:'全国杯', date: '11月后', type: 'GI'},
        {id:7101, name:'长途锦标赛', date: '12月前', type: 'GII'},
		{id:7102, name:'挑战杯', date: '12月前', type: 'GIII'},
        {id:7103, name:'中日新闻杯', date: '12月前', type: 'GIII'},
		{id:7104, name:'五车二锦标赛', date: '12月前', type: 'GIII'},
		{id:7105, name:'绿松石锦标赛', date: '12月前', type: 'GIII'},
        {id:7111, name:'全国冠军杯', date: '12月前', type: 'GI'},
        {id:7201, name:'阪神杯', date: '12月后', type: 'GII'},
        {id:7204, name:'中山大奖赛', date: '12月后', type: 'GI'},
        {id:7205, name:'东京大奖赛', date: '12月后', type: 'GI'}],
      cultivatePresets:[],
      cultivateDefaultPresets:[
      {
          name: "默认",
          race_list: [],
          skill: "",
          expect_attribute:[800, 800, 800, 400, 400],
          follow_support_card: {id:1, name:'在耀眼景色的前方'},
          follow_support_card_level: 50,
          clock_use_limit: 99,
          learn_skill_threshold: 9999,
          race_tactic_1: 4,
          race_tactic_2: 4,
          race_tactic_3: 4,

        },
        {
          name: "小栗帽基础育成赛程",
          race_list: [1701, 2303, 2401, 5208, 5407, 5904],
          skill: "",
          expect_attribute:[800, 650, 800, 300, 400],
          follow_support_card: {id:16, name:'一颗安心糖'},
          follow_support_card_level: 50,
          clock_use_limit: 99,
          learn_skill_threshold: 9999,
          race_tactic_1: 4,
          race_tactic_2: 4,
          race_tactic_3: 4,
        },
        {
          name: "大和赤骥基础育成赛程",
          race_list: [1701, 2303],
          skill: "",
          expect_attribute:[800, 600, 600, 300, 400],
          follow_support_card: {id:16, name:'一颗安心糖'},
          follow_support_card_level: 50,
          clock_use_limit: 99,
          learn_skill_threshold: 9999,
          race_tactic_1: 4,
          race_tactic_2: 4,
          race_tactic_3: 4,
        },
        {
          name: "目白麦昆基础育成赛程",
          race_list: [2203, 2401],
          skill: "",
          expect_attribute:[700, 700, 600, 350, 400],
          follow_support_card: {id:16, name:'一颗安心糖'},
          follow_support_card_level: 50,
          clock_use_limit: 99,
          learn_skill_threshold: 9999,
          race_tactic_1: 4,
          race_tactic_2: 4,
          race_tactic_3: 4,
        },
        {
          name:"Veteran Oguri Cap 35 Races 600k Fans (Requires Awakening 3, Max Limit Break Super Creek, Speed/Stamina Stallion, Support Cards with High Race Bonus)",
          race_list:[1601,1701,1902,2103,2302,2401,2701,2905,3103,3303,3404,3601,4102,4203,4408,4506,4607,4804,4902,5208,5407,5601,5709,5904,6006,6602,6701,6807,7007,7111,7204],
          skill:"Big Eater",
          expect_attribute:[700,500,700,350,350],
          follow_support_card:{"id":16,"name":"A Reassuring Candy","desc":"Stamina Super Creek"},
          follow_support_card_level:50,
          clock_use_limit:2,
          learn_skill_threshold:450,
          race_tactic_1:4,
          race_tactic_2:3,
          race_tactic_3:3
        }
      ],
      expectSpeedValue : 650,
      expectStaminaValue : 600,
      expectPowerValue: 650,
      expectWillValue: 300,
      expectIntelligenceValue:300,

      supportCardLevel: 50,
      
      presetsUse: {
          name: "默认",
          race_list: [],
          skill: "",
          skill_priority_list:[],
          skill_blacklist: "",
          expect_attribute:[650, 800, 650, 400, 400],
          follow_support_card: {id:1, name:'在耀眼景色的前方'},
          follow_support_card_level: 50,
          clock_use_limit: 99,
          learn_skill_threshold: 9999,
          race_tactic_1: 4,
          race_tactic_2: 4,
          race_tactic_3: 4,
          extraWeight:[],
        },
      // ===  已选择  ===
      selectedExecuteMode: 1,
      expectTimes: 0,
      cron: "* * * * *",
      
      selectedUmamusumeTaskType: undefined,
      selectedSupportCard: undefined,
      extraRace: [],
      skillLearnPriorityList:[
					{
						priority:0,
						skills:""
					}
				],
      skillPriorityNum:1,
      skillLearnBlacklist:"",
      learnSkillOnlyUserProvided: false,
      learnSkillBeforeRace: false,
      selectedRaceTactic1: 4,
      selectedRaceTactic2: 4,
      selectedRaceTactic3: 4,
      clockUseLimit: 99,
      learnSkillThreshold: 9999,
      recoverTP: false,
      presetNameEdit: "",
      successToast: undefined,
      extraWeight1: [0, 0, 0, 0, 0],
      extraWeight2: [0, 0, 0, 0, 0],
      extraWeight3: [0, 0, 0, 0, 0],
    }
  },
  mounted() {
    this.initSelect()
    this.getPresets()
    this.successToast = $('.toast').toast({})
  },
  methods:{
    deleteBox(item,index){
        if(this.skillLearnPriorityList.length<=1){
          return false
        }
        this.skillLearnPriorityList.splice(index,1)
        this.skillPriorityNum--
        for(let i = index; i < this.skillPriorityNum; i++)
        {
          this.skillLearnPriorityList[i].priority--
        }
      },
    addBox(item){
        if(this.skillLearnPriorityList.length>=5)
        {
          return false
        }
        this.skillLearnPriorityList.push(
          {
            priority:this.skillPriorityNum++,
            skills:''
          }
        )
    },
    initSelect: function (){
      this.selectedSupportCard = this.umausumeSupportCardList[0]
      this.selectedUmamusumeTaskType = this.umamusumeTaskTypeList[0]
    },
    switchRaceList: function(){
      this.showRaceList = !this.showRaceList
    },
    switchAdvanceOption: function(){
      this.showAdvanceOption = !this.showAdvanceOption
    },
    addTask: function (){
      var learn_skill_list = []
      for (let i = 0; i < this.skillPriorityNum; i++)
      {
        if(String(this.skillLearnPriorityList[i].skills) != "")
        {
          learn_skill_list.push(String(this.skillLearnPriorityList[i].skills).split(",").map(item => item.trim()))
        }
      }
      console.log(learn_skill_list)
      var learn_skill_blacklist = this.skillLearnBlacklist ? this.skillLearnBlacklist.split(",").map(item => item.trim()) : []
      let payload = {
        app_name: "umamusume",
        task_execute_mode: this.selectedExecuteMode,
        task_type: this.selectedUmamusumeTaskType.id,
        task_desc: this.selectedUmamusumeTaskType.name,
        attachment_data: {
          "expect_attribute": [this.expectSpeedValue, this.expectStaminaValue, this.expectPowerValue, this.expectWillValue, this.expectIntelligenceValue],
          "follow_support_card_name": this.selectedSupportCard.name,
          "follow_support_card_level": this.supportCardLevel,
          "extra_race_list": this.extraRace,
          "learn_skill_list": learn_skill_list,
          "learn_skill_blacklist": learn_skill_blacklist,
          "tactic_list": [this.selectedRaceTactic1, this.selectedRaceTactic2, this.selectedRaceTactic3],
          "clock_use_limit": this.clockUseLimit,
          "learn_skill_threshold": this.learnSkillThreshold,
          "allow_recover_tp": this.recoverTP,
          "learn_skill_only_user_provided": this.learnSkillOnlyUserProvided,
          "extra_weight": [this.extraWeight1, this.extraWeight2, this.extraWeight3]
        },
        cron_job_info:{},
      }
      if(this.selectedExecuteMode === 2){
        payload.cron_job_info = {
          cron: this.cron
        }
      }
      console.log(JSON.stringify(payload))
      this.axios.post("/task", JSON.stringify(payload)).then(
          ()=>{
            $('#create-task-list-modal').modal('hide');
          }
      )
    },
    applyPresetRace: function(){
      this.extraRace = this.presetsUse.race_list
      this.expectSpeedValue = this.presetsUse.expect_attribute[0]
      this.expectStaminaValue = this.presetsUse.expect_attribute[1]
      this.expectPowerValue = this.presetsUse.expect_attribute[2]
      this.expectWillValue = this.presetsUse.expect_attribute[3]
      this.expectIntelligenceValue = this.presetsUse.expect_attribute[4]
      this.selectedSupportCard = this.presetsUse.follow_support_card,
      this.supportCardLevel = this.presetsUse.follow_support_card_level,
      this.clockUseLimit = this.presetsUse.clock_use_limit,
      this.learnSkillThreshold = this.presetsUse.learn_skill_threshold,
      this.selectedRaceTactic1 = this.presetsUse.race_tactic_1,
      this.selectedRaceTactic2 = this.presetsUse.race_tactic_2,
      this.selectedRaceTactic3 = this.presetsUse.race_tactic_3,
      this.skillLearnBlacklist = this.presetsUse.skill_blacklist

      if ('extraWeight' in this.presetsUse && this.presetsUse.extraWeight != [])
      {
        this.extraWeight1 =  this.presetsUse.extraWeight[0]
        this.extraWeight2 =  this.presetsUse.extraWeight[1]
        this.extraWeight3 =  this.presetsUse.extraWeight[2]
      }
      else
      {
        this.extraWeight1 = [0,0,0,0,0]
        this.extraWeight2 = [0,0,0,0,0]
        this.extraWeight3 = [0,0,0,0,0]
      }
      if ('skill' in this.presetsUse && this.presetsUse.skill != "")
      {
        this.skillLearnPriorityList[0].skills = this.presetsUse.skill
        while(this.skillPriorityNum > 1)
        {
          this.deleteBox(0,this.skillPriorityNum-1)
        }
      }
      else
      {
        for (let i = 0; i < this.presetsUse.skill_priority_list.length; i++)
        {
          if (i >= this.skillPriorityNum)
          {
            this.addBox()
          }
          this.skillLearnPriorityList[i].skills = this.presetsUse.skill_priority_list[i]
        }
        while(this.presetsUse.skill_priority_list.length != 0 &&
              this.skillPriorityNum > this.presetsUse.skill_priority_list.length)
        {
          this.deleteBox(0,this.skillPriorityNum-1)
        }
      }
      
    },
    getPresets: function(){
      this.axios.post("/umamusume/get-presets", "").then(
          res=>{
          let tmplist = []
          tmplist = tmplist.concat(this.cultivateDefaultPresets)
          tmplist = tmplist.concat(res.data)
          this.cultivatePresets = tmplist
        }
      )
    },
    addPresets: function(){
      let preset = {
        name: this.presetNameEdit,
        race_list: this.extraRace,
        skill_priority_list: [],
        skill_blacklist: this.skillLearnBlacklist,
        expect_attribute:[this.expectSpeedValue, this.expectStaminaValue, this.expectPowerValue, this.expectWillValue, this.expectIntelligenceValue],
        follow_support_card: this.selectedSupportCard,
        follow_support_card_level: this.supportCardLevel,
        clock_use_limit: this.clockUseLimit,
        learn_skill_threshold: this.learnSkillThreshold,
        race_tactic_1: this.selectedRaceTactic1,
        race_tactic_2: this.selectedRaceTactic2,
        race_tactic_3: this.selectedRaceTactic3,
        extraWeight: [this.extraWeight1,this.extraWeight2,this.extraWeight3]
      }
      for(let i = 0; i < this.skillPriorityNum; i++)
      {
        if(this.skillLearnPriorityList[i].skills != "")
        {
          preset.skill_priority_list.push([this.skillLearnPriorityList[i].skills])
        }
      }
      let payload = {
        "preset": JSON.stringify(preset)
      }
      console.log(JSON.stringify(payload))
      this.axios.post("/umamusume/add-presets", JSON.stringify(payload)).then(
        ()=>{
          this.successToast.toast('show')
          this.getPresets()
        } 
      )
    }
  },
  watch:{

  }
}
</script>

<style scoped>

.btn{
  padding: 0.4rem 0.8rem !important;
  font-size: 1rem !important;
}

.red-button {
  background-color: red !important;
  padding: 0.4rem 0.8rem !important;
  font-size: 1rem !important;
  border-radius: 0.25rem;
}

</style>