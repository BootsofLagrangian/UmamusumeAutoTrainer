from bot.base.context import BotContext
from module.umamusume.task import UmamusumeTask, UmamusumeTaskType
from module.umamusume.define import *
import bot.base.log as logger

log = logger.get_logger(__name__)


class SupportCardInfo:
    name: str
    card_type: SupportCardType
    favor: SupportCardFavorLevel
    has_event: bool

    def __init__(self,
                 name: str = "support_card",
                 card_type: SupportCardType = SupportCardType.SUPPORT_CARD_TYPE_UNKNOWN,
                 favor: SupportCardFavorLevel = SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_UNKNOWN,
                 has_event: bool = False):
        self.name = name
        self.card_type = card_type
        self.favor = favor
        self.has_event = has_event


class TrainingInfo:
    support_card_info_list: list[SupportCardInfo]
    speed_incr: int
    stamina_incr: int
    power_incr: int
    will_incr: int
    intelligence_incr: int
    skill_point_incr: int

    def __init__(self):
        self.speed_incr = 0
        self.stamina_incr = 0
        self.power_incr = 0
        self.will_incr = 0
        self.intelligence_incr = 0
        self.skill_point_incr = 0
        self.support_card_info_list = []

    def log_training_info(self):
        log.info("트레이닝 결과: 스피드: %s, 스태미나: %s, 파워: %s, 근성: %s, 지능: %s, 스킬 포인트: %s", self.speed_incr,
                 self.stamina_incr, self.power_incr, self.will_incr,
                 self.intelligence_incr, self.skill_point_incr)
        text = "이 트레이닝의 서포트 카드: ["
        for c in self.support_card_info_list:
            if c.favor != SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_UNKNOWN:
                text += "[서포트 카드 이름: " + str(c.name) + " 서포트 카드 타입: " + str(c.card_type.name) + ", 서포트 카드 호감도: " + str(c.favor.name) + "] "
        text += "]"
        log.info(text)


class UmaAttribute:
    speed: int
    stamina: int
    power: int
    will: int
    intelligence: int
    skill_point: int

    def __init__(self):
        self.speed = 0
        self.stamina = 0
        self.power = 0
        self.will = 0
        self.intelligence = 0
        self.skill_point = 0


class TurnOperation:
    turn_operation_type: TurnOperationType
    turn_operation_type_replace: TurnOperationType
    training_type: TrainingType
    race_id: int

    def __init__(self):
        self.turn_operation_type = TurnOperationType.TURN_OPERATION_TYPE_UNKNOWN
        self.turn_operation_type_replace = TurnOperationType.TURN_OPERATION_TYPE_UNKNOWN
        self.training_type = TrainingType.TRAINING_TYPE_UNKNOWN
        self.race_id = 0

    def log_turn_operation(self):
        log.info("이번 턴 작업: %s", self.turn_operation_type.name)
        log.info("이번 턴 대체 작업: %s", self.turn_operation_type_replace.name)
        if self.turn_operation_type == TurnOperationType.TURN_OPERATION_TYPE_TRAINING:
            log.info("트레이닝 타입: %s", self.training_type.name)


class TurnInfo:
    date: int

    parse_train_info_finish: bool
    training_info_list: list[TrainingInfo]
    parse_main_menu_finish: bool
    uma_attribute: UmaAttribute
    remain_stamina: int
    motivation_level: MotivationLevel
    medic_room_available: bool
    race_available: bool

    turn_operation: TurnOperation | None
    turn_info_logged: bool
    turn_learn_skill_done: bool

    def __init__(self):
        self.date = -1
        self.parse_train_info_finish = False
        self.training_info_list = [TrainingInfo(), TrainingInfo(), TrainingInfo(), TrainingInfo(), TrainingInfo()]
        self.parse_main_menu_finish = False
        self.uma_attribute = UmaAttribute()
        self.remain_stamina = -1
        self.motivation_level = MotivationLevel.MOTIVATION_LEVEL_UNKNOWN
        self.medic_room_available = False
        self.race_available = False
        self.turn_operation = None
        self.turn_info_logged = False
        self.turn_learn_skill_done = False

    def log_turn_info(self):
        log.info("현재 턴 시간: " + str(self.date))
        log.info("동기 상태: " + str(self.motivation_level.name))
        log.info("남은 스태미나: " + str(self.remain_stamina))
        log.info("현재 속성 값 - 스피드: %s, 스태미나: %s, 파워: %s, 근성: %s, 지능: %s, 스킬 포인트: %s", self.uma_attribute.speed,
                 self.uma_attribute.stamina, self.uma_attribute.power, self.uma_attribute.will, self.uma_attribute.intelligence, self.uma_attribute.skill_point)
        log.info("스피드 트레이닝 결과:")
        self.training_info_list[0].log_training_info()
        log.info("스태미나 트레이닝 결과:")
        self.training_info_list[1].log_training_info()
        log.info("파워 트레이닝 결과:")
        self.training_info_list[2].log_training_info()
        log.info("근성 트레이닝 결과:")
        self.training_info_list[3].log_training_info()
        log.info("지능 트레이닝 결과:")
        self.training_info_list[4].log_training_info()


class CultivateContextDetail:
    turn_info: TurnInfo | None
    turn_info_history: list[TurnInfo]
    expect_attribute: list[int] | None
    follow_support_card_name: str
    follow_support_card_level: int
    extra_race_list: list[int]
    learn_skill_list: list[list[str]]
    learn_skill_blacklist: list[str]
    learn_skill_done: bool
    learn_skill_selected: bool
    cultivate_finish: bool
    tactic_list: list[int]
    debut_race_win: bool
    clock_use_limit: int
    clock_used: int
    learn_skill_threshold: int
    learn_skill_only_user_provided: bool
    learn_skill_before_race: bool
    allow_recover_tp: bool
    parse_factor_done: bool
    extra_weight: list

    def __init__(self):
        self.expect_attribute = None
        self.turn_info = TurnInfo()
        self.turn_info_history = []
        self.extra_race_list = []
        self.learn_skill_list = []
        self.learn_skill_blacklist = []
        self.learn_skill_done = False
        self.learn_skill_selected = False
        self.cultivate_finish = False
        self.tactic_list = []
        self.debut_race_win = False
        self.clock_use_limit = 0
        self.clock_used = 0
        self.allow_recover_tp = False
        self.parse_factor_done = False
        self.extra_weight = []

    def reset_skill_learn(self):
        self.learn_skill_done = False
        self.learn_skill_selected = False


class UmamusumeContext(BotContext):
    task: UmamusumeTask
    cultivate_detail: CultivateContextDetail

    def __init__(self, task, ctrl):
        super().__init__(task, ctrl)

    def is_task_finish(self) -> bool:
        return False


def build_context(task: UmamusumeTask, ctrl) -> UmamusumeContext:
    ctx = UmamusumeContext(task, ctrl)
    if task.task_type == UmamusumeTaskType.UMAMUSUME_TASK_TYPE_CULTIVATE:
        detail = CultivateContextDetail()
        detail.expect_attribute = task.detail.expect_attribute
        detail.follow_support_card_name = task.detail.follow_support_card_name
        detail.follow_support_card_level = task.detail.follow_support_card_level
        detail.extra_race_list = task.detail.extra_race_list
        detail.learn_skill_list = task.detail.learn_skill_list
        detail.learn_skill_blacklist = task.detail.learn_skill_blacklist
        detail.tactic_list = task.detail.tactic_list
        detail.clock_use_limit = task.detail.clock_use_limit
        detail.learn_skill_threshold = task.detail.learn_skill_threshold
        detail.learn_skill_only_user_provided = task.detail.learn_skill_only_user_provided
        detail.allow_recover_tp = task.detail.allow_recover_tp
        detail.extra_weight = task.detail.extra_weight
        ctx.cultivate_detail = detail
    return ctx





