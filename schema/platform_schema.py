import sgqlc.types


platform_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class AppKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ENTERPRISE', 'SELF', 'THIRD_PARTY')


class AppVersionStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('OFFLINE', 'ONLINE', 'PENDING')


class AuthenticationConfigurationKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('OAUTH_2', 'OPENID_CONNECT_1')


class AuthenticationMethod(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('BASIC_HTTP_AUTHENTICATION_SCHEME', 'POST_IN_FORM')


class AuthenticationSourceKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('LDAP_3', 'OAUTH_2', 'OPENID_CONNECT_1', 'SAML_2')


class BacklogStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FINISHED', 'PENDING')


class BarCodeType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CODE128', 'QRCODE')


Boolean = sgqlc.types.Boolean

class BorrowState(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('IS_BORROWED', 'IS_RETURN', 'NOT_CONFIRMED')


class CalibrateMethod(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('EXEMPTION', 'INSIDE', 'OUTSIDE', 'UNSET')


class CalibrateReason(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('BORROWED', 'EXPIRED', 'LEASED', 'NEW', 'OTHER', 'REPAIR')


class CalibrateRepeatPeriod(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('MONTH', 'YEAR')


class CalibrateResult(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('BY_RESULT', 'QUALIFIED', 'UNQUALIFIED', 'UNSET')


class CalibrateState(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CALIBRATING', 'DONE', 'UNSET')


class CertificateState(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('NOT_RETURNED', 'RETURNED')


class ChangeBorrowOperatorType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APPROVE', 'REJECT', 'SUBMIT')


class ChangeBorrowState(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FINISHED', 'NOT_PASS', 'PENDING', 'UNDER_REVIEW_BY_APPLY_FOR', 'UNDER_REVIEW_BY_BORROWED')


class ChangeBorrowTrigger(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APPROVE', 'REJECT', 'SAVE', 'SUBMIT')


class ChannelStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('AVAILABLE', 'UNAVAILABLE')


class CodePrefix(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('GZ', 'LJ', 'ZL')


class CodeRuleConfigurationColumn(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CODE_PREFIX', 'FIXED_FIELD', 'PURCHASE', 'SERIAL_NUMBER', 'THING_CATEGORY', 'THING_DEPARTMENT')


class CodeRuleConfigurationRule(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('AUTOGENERATE_CANNOT_MODIFY', 'AUTOGENERATE_CAN_MODIFY', 'BY_HAND')


class DatetimeFormat(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('MMDD', 'YY', 'YYMM', 'YYMMDD', 'YYYY', 'YYYYMM', 'YYYYMMDD')


class DeleteThingLimitedReason(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('THING_BORROW', 'THING_CALIBRATE', 'THING_INSPECTION', 'THING_INVENTORY', 'THING_MAINTENANCE')


class DifferenceResult(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ADDED', 'REMOVED')


class EamAttachmentType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('AUDIO', 'CUSTOM', 'DOC', 'PIC', 'VIDEO', 'ZIP')


class EamFieldGroupType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ATTACHMENT', 'CALIBRATE', 'FINANCIAL', 'FOUNDATION', 'MAINTENANCE', 'MANAGEMENT', 'PURCHASE')


class EamFieldType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ATTACHMENT', 'CATEGORY', 'DATE', 'DATE_SET', 'DEPARTMENT', 'LABEL', 'LABEL_TEXT_SET', 'MULTI_RADIO', 'MULTI_RADIO_DATE_SET', 'MULTI_RADIO_TEXT_SET', 'NUMBER', 'OTHER', 'RADIO', 'RANGE', 'SELECT_BOX', 'SELECT_DATE_SET', 'SELECT_TEXT_SET', 'TEXT', 'TEXT_SET')


class EamImportOption(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('INSERT_NORMAL', 'UPSERT_NORMAL')


class EamWorkflowDefaultReviewOperate(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ABORT', 'AUTO_APPROVE', 'SPECIFIC')


class EamWorkflowReviewer(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('KEEPER', 'OFFICER')


class EamWorkflowReviewerLevel(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FIRST', 'PRESENT', 'SECOND')


Float = sgqlc.types.Float

class Granularity(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ANNUALLY', 'DAILY', 'FIVE_MINUTE', 'HOURLY', 'MINUTE', 'MONTHLY', 'WEEKLY')


ID = sgqlc.types.ID

Int = sgqlc.types.Int

class JSON(sgqlc.types.Scalar):
    __schema__ = platform_schema


class JSONString(sgqlc.types.Scalar):
    __schema__ = platform_schema


class JumpKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CURRENT_WINDOW', 'NEW_WINDOW')


class LDAP3EncryptionMethod(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('NONE', 'SSL', 'STARTTLS')


class LogAction(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CREATE', 'DELETE', 'LOGIN', 'LOGOUT', 'READ', 'UPDATE')


class LoginConfigurationKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('OAUTH_2', 'OPENID_CONNECT_1', 'SYSTEM')


class LoginMode(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCOUNT_PASSWORD', 'DINGDING', 'EMAIL_PASSWORD', 'PHONE_VERIFY_CODE', 'SSO', 'WECHAT')


class MessageChannelKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('EMAIL', 'INBOX', 'WECOM')


class MessageKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FILE', 'IMAGE', 'TEXT', 'TEXT_CARD', 'VIDEO')


class OnState(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ABANDONED', 'AVAILABLE', 'DEBUGGING', 'IN_USE', 'OFF_LEASE', 'OTHER', 'PENDING', 'PROCESSED', 'REPAIRING', 'STOCK_IN')


class OpenIDConnect1ConfigurationMethod(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DISCOVERY', 'MANUAL')


class OutsideCalibratePayStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('PAID', 'UNDER_REVIEW')


class PermissionType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FEATURE', 'MENU', 'PAGE')


class PushScheduleType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CRON', 'IMMEDIATELY')


class RepeatPeriod(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DAY', 'MONTH', 'WEEK', 'YEAR')


class ResponseFormat(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FORM', 'JSON')


class ReturnState(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('NOT_RETURNED', 'RETURNED')


class SetOption(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ADD', 'REPLACE')


class SparePartClaimOperatorType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APPROVE', 'CANCEL', 'CONFIRM', 'ISSUE', 'RECORD', 'REJECT', 'SUBMIT', 'WITHDRAW')


class SparePartClaimReason(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('MAINTENANCE', 'OTHER', 'REPAIR', 'UPGRADE')


class SparePartClaimStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('COMPLETED', 'ISSUING', 'PENDING', 'UNDER_CONFIRM', 'UNDER_ISSUE', 'UNDER_REVIEW', 'WITHDRAWED')


class SparePartDefaultReviewOperate(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('AUTO_APPROVE', 'SPECIFIC')


class SparePartOutboundKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CLAIM', 'TRANSFER')


class SparePartReceiptKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('OTHER', 'PURCHASE', 'RETURN', 'TRANSFER')


class SparePartStockRecordType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('OUTBOUND', 'RECEIPT')


class SparePartStockScope(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ALL', 'SPECIFIC')


class SparePartWriteoffKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('OUTBOUND', 'RECEIPT')


class StaffJobStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ON_THE_JOB', 'RESIGNED')


class StaffJobType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('EXTERNAL', 'FORMAL', 'INFORMAL')


String = sgqlc.types.String

class TableFieldGroup(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CUSTOM', 'FIXED', 'SCROLLABLE')


class TemplateStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DISABLED', 'ENABLED')


class TenantCertificationStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CERTIFIED', 'PENDING', 'REJECTED', 'UNCERTIFIED')


class TenantStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DISABLED', 'ENABLED')


class TenantType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('COMPANY', 'PLATFORM')


class ThingAccountType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FIXED', 'LOW_VALUE_CONSUMABLES')


class ThingBarLabelSection(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('BAR', 'FIELD', 'LOGO')


class ThingBarLabelTemplate(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CODE128', 'LR_FIELD_QRCODE', 'LR_LOGO_FIELD_QRCODE', 'QRCODE', 'TB_FIELD_CODE128', 'TB_LOGO_FIELD_CODE128')


class ThingBorrowOperatorType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APPROVE', 'BORROW_CONFIRMATION', 'EVALUATION', 'FOUND', 'LOST_CONFIRMATION', 'LOST_REPORT', 'QUALIFIED', 'REJECT', 'REPLACE', 'RETURN_CONFIRMATION', 'RETURN_REPORT', 'SUBMIT', 'UNQUALIFIED', 'WITHDRAW')


class ThingBorrowState(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('BORROW_CONFIRMATION', 'BORROW_EVALUATION', 'FINISHED_LOST', 'FINISHED_RETURNED', 'FINISHED_WITHDRAWED', 'LENT', 'LOST_CONFIRMATION', 'PENDING', 'RETURN_CONFIRMATION', 'RETURN_EVALUATION', 'UNDER_REVIEW_BY_APPLY_FOR', 'UNDER_REVIEW_BY_BORROWED', 'UNDER_REVIEW_BY_KEEPER')


class ThingBorrowStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('LENT', 'LOST', 'PENDING', 'RETURNED', 'UNDER_REVIEW', 'WITHDRAWED')


class ThingBorrowTrigger(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APPROVE', 'REJECT', 'SAVE', 'SUBMIT', 'WITHDRAW')


class ThingCalibrateOperatorType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APPROVE', 'RECORD', 'REJECT', 'SUBMIT', 'TURNTO')


class ThingCalibrateState(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CALIBRATE_BEGIN', 'CALIBRATE_FINISHED', 'CALIBRATE_UNDER_REVIEW')


class ThingCalibrateStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FINISHED', 'PENDING', 'UNDER_REVIEW')


class ThingCategoryLevel(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CURRENT', 'FIRST', 'SECOND')


class ThingDepartmentScope(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ALL', 'DEPARTMENT', 'DEPARTMENT_WITH_SUBORDINATE', 'NONE')


class ThingGroupAlterOperation(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ADD', 'REMOVE')


class ThingGroupType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DEPARTMENT', 'PERSONAL')


class ThingInspectionCreateType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('BYHANDLE', 'BYSCHEDULE')


class ThingInspectionOperatorType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPT', 'FINISH', 'RESTART', 'TURNTO')


class ThingInspectionStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FINISHED', 'INSPECTING', 'PENDING')


class ThingInspectionTrigger(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPT', 'FINISH', 'RESTART', 'SAVE', 'TURNTO')


class ThingInventoryConstraint(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('UPLOAD_IMAGE',)


class ThingInventoryLabel(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ABANDONED', 'INCONSISTENT', 'MAINTENANCE', 'OTHER', 'RELABEL', 'REPAIR')


class ThingInventoryMethod(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('MANUAL', 'SCAN', 'SCAN_AND_MANUAL')


class ThingInventoryState(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FINISHED', 'LACK', 'UN_FINISHED')


class ThingInventoryTicketState(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FINISHED', 'IN_PROGRESS', 'PENDING')


class ThingInventoryUserScope(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('MANAGER', 'MANAGER_AND_MAINTAINER')


class ThingMaintenanceCreateType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('BYHANDLE', 'BYSCHEDULE')


class ThingMaintenanceOperatorType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPT', 'APPLY_FOR_SPARE_PART', 'APPROVE', 'FINISH', 'PAUSE', 'REJECT', 'RESTART', 'TURNTO')


class ThingMaintenanceStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FINISHED', 'MAINTAINING', 'PAUSED', 'PENDING', 'UNDER_REVIEW')


class ThingMaintenanceTrigger(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPT', 'APPROVE', 'FINISH', 'PAUSE', 'REJECT', 'RESTART', 'SAVE', 'TURNTO')


class ThingPerformanceStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ERROR', 'GOOD')


class ThingPurchaseType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('LEASED', 'MAKE_BY_SELF', 'OUTSOURCING')


class ThingRepairOperatorType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPT', 'APPLY_FOR_SPARE_PART', 'APPROVE', 'FINISH', 'PAUSE', 'REJECT', 'RESTART', 'TURNTO')


class ThingRepairStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FINISHED', 'PAUSED', 'PENDING', 'REPAIRING', 'UNDER_REVIEW')


class ThingRepairTrigger(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPT', 'APPROVE', 'FINISH', 'PAUSE', 'REJECT', 'RESTART', 'SAVE', 'TURNTO')


class ThingRepairType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('NOREPAIR', 'REPAIR', 'REPAIROUTSOURCE')


class ThingStorageType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('PERSONAL', 'PUBLIC')


class ThingTransferType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ABANDONED', 'BORROW', 'FOUND', 'LOST', 'RETURN', 'TRANSFER')


class ThingWarrantyMethod(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('NO', 'ORIGINAL_FACTORY', 'SPECIFIED')


class TicketType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('INSPECTION', 'MAINTENANCE')


class Timestamp(sgqlc.types.Scalar):
    __schema__ = platform_schema


class TimestampRange(sgqlc.types.Scalar):
    __schema__ = platform_schema


class UCCAttachmentType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('AUDIO', 'CUSTOM', 'DOC', 'PIC', 'VIDEO', 'ZIP')


class UCCFieldType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ATTACHMENT', 'DATE', 'LABEL', 'MULTI_RADIO', 'RADIO', 'RANGE', 'RANGE_EXTREMUM', 'SELECT_BOX', 'SET', 'TEXT')


class UCCFiledValue(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FLOAT', 'TEXT')


class UCCScope(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('COMPANY', 'PLATFORM')


class UserInfoRequestMethod(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('GET', 'POST')




########################################################################
# Input Objects
########################################################################
class AccountListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('is_allowed_to_login', 'only_no_roles', 'roles', 'search', 'search_by')
    is_allowed_to_login = sgqlc.types.Field(Boolean, graphql_name='isAllowedToLogin')
    only_no_roles = sgqlc.types.Field(Boolean, graphql_name='onlyNoRoles')
    roles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='roles')
    search = sgqlc.types.Field(String, graphql_name='search')
    search_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='searchBy')


class AddAccountRolesInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account_ids', 'role_ids')
    account_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='accountIds')
    role_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='roleIds')


class AddBacklogToUsers(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('backlog', 'users')
    backlog = sgqlc.types.Field(sgqlc.types.non_null('BacklogInput'), graphql_name='backlog')
    users = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput'))), graphql_name='users')


class AddFeaturePackToTenant(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('expired_at', 'feature_pack', 'is_always_effective', 'tenant')
    expired_at = sgqlc.types.Field(Timestamp, graphql_name='expiredAt')
    feature_pack = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='featurePack')
    is_always_effective = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAlwaysEffective')
    tenant = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='tenant')


class AddThingBorrowDraftInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('add_sub_thing', 'code', 'company', 'department', 'expected_borrow_at', 'expected_return_at', 'thing')
    add_sub_thing = sgqlc.types.Field(Boolean, graphql_name='addSubThing')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    department = sgqlc.types.Field('IDInput', graphql_name='department')
    expected_borrow_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='expectedBorrowAt')
    expected_return_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='expectedReturnAt')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='thing')


class AddThingChangeBorrowDraftInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('change_return_at', 'code', 'company', 'thing', 'thing_circulation')
    change_return_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='changeReturnAt')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='thing')
    thing_circulation = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput'))), graphql_name='thingCirculation')


class AddThingTransferRecordByCodeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('records', 'thing_code')
    records = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingTransferRecordInput'))), graphql_name='records')
    thing_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='thingCode')


class AddThingTransferRecordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('records', 'thing')
    records = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingTransferRecordInput'))), graphql_name='records')
    thing = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='thing')


class ApiFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class AppListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class AppVersionListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app_id',)
    app_id = sgqlc.types.Field(String, graphql_name='appId')


class ApplyForTenantCertificationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('business_license_image', 'tenant_id')
    business_license_image = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='businessLicenseImage')
    tenant_id = sgqlc.types.Field(String, graphql_name='tenantId')


class ApproveChangeBorrowInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'opinion')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    opinion = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='opinion')


class ApproveThingCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'id', 'is_synchronized', 'remark')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='attachment')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_synchronized = sgqlc.types.Field(Boolean, graphql_name='isSynchronized')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class AssignAppPermissionsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app', 'permissions')
    app = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='app')
    permissions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput'))), graphql_name='permissions')


class AssignTenantAppsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('apps', 'tenant')
    apps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput'))), graphql_name='apps')
    tenant = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='tenant')


class AuthorizationRuleAndDependenciesOfUserFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'permission_types', 'user_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    permission_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PermissionType)), graphql_name='permissionTypes')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')


class AuthorizationRuleFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app_ids', 'is_leaf_only', 'permission_types', 'require_data_ranges', 'search')
    app_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='appIds')
    is_leaf_only = sgqlc.types.Field(Boolean, graphql_name='isLeafOnly')
    permission_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PermissionType)), graphql_name='permissionTypes')
    require_data_ranges = sgqlc.types.Field(Boolean, graphql_name='requireDataRanges')
    search = sgqlc.types.Field(String, graphql_name='search')


class BIFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('aggregation', 'end', 'granularity', 'metric', 'series', 'start')
    aggregation = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='aggregation')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    granularity = sgqlc.types.Field(Granularity, graphql_name='granularity')
    metric = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='metric')
    series = sgqlc.types.Field(String, graphql_name='series')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')


class BacklogFieldDataInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class BacklogInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('data', 'group', 'id', 'title', 'url')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BacklogFieldDataInput)), graphql_name='data')
    group = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='group')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class CalibrateOrganizationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')


class CalibrateRepeatInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('frequency', 'period')
    frequency = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='frequency')
    period = sgqlc.types.Field(sgqlc.types.non_null(CalibrateRepeatPeriod), graphql_name='period')


class CalibrateScheduleFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class ChangeBorrowApproveConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ChangeBorrowState)), graphql_name='source')


class ChangeBorrowItemListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('change_borrow',)
    change_borrow = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='changeBorrow')


class ChangeBorrowListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('applicant', 'company', 'department_of_applicant', 'department_of_manager', 'end_at', 'search', 'start_at', 'state')
    applicant = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='applicant')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    department_of_applicant = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='departmentOfApplicant')
    department_of_manager = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='departmentOfManager')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    state = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ChangeBorrowState)), graphql_name='state')


class ChangeMyPasswordByEmailVerificationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('email', 'new_password', 'verify_code')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    new_password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='newPassword')
    verify_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='verifyCode')


class ChangeMyPasswordByVerifyCodeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('new_password', 'verify_code')
    new_password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='newPassword')
    verify_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='verifyCode')


class ChangeMyPasswordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('new_password', 'old_password')
    new_password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='newPassword')
    old_password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='oldPassword')


class CheckAlterDepartmentThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('children_depts', 'current_dept', 'operation', 'parent_dept', 'thing_group')
    children_depts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='childrenDepts')
    current_dept = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='currentDept')
    operation = sgqlc.types.Field(sgqlc.types.non_null(ThingGroupAlterOperation), graphql_name='operation')
    parent_dept = sgqlc.types.Field('IDInput', graphql_name='parentDept')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='thingGroup')


class CityFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('province',)
    province = sgqlc.types.Field('StringIDInput', graphql_name='province')


class CodeColumnConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('category_length', 'category_level', 'column_type', 'connector', 'content', 'format', 'length', 'need_connector', 'order_number', 'relate_column', 'start_number')
    category_length = sgqlc.types.Field(Int, graphql_name='categoryLength')
    category_level = sgqlc.types.Field(ThingCategoryLevel, graphql_name='categoryLevel')
    column_type = sgqlc.types.Field(sgqlc.types.non_null(CodeRuleConfigurationColumn), graphql_name='columnType')
    connector = sgqlc.types.Field(String, graphql_name='connector')
    content = sgqlc.types.Field(String, graphql_name='content')
    format = sgqlc.types.Field(DatetimeFormat, graphql_name='format')
    length = sgqlc.types.Field(Int, graphql_name='length')
    need_connector = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='needConnector')
    order_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='orderNumber')
    relate_column = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CodeRuleConfigurationColumn)), graphql_name='relateColumn')
    start_number = sgqlc.types.Field(Int, graphql_name='startNumber')


class CompanyBIDatasourceFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')


class CompanyFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids', 'search')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids')
    search = sgqlc.types.Field(String, graphql_name='search')


class CompanyLoginInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account', 'company_uid', 'password')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    company_uid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='companyUID')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')


class CompanyThingCategoryUCCFieldListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')


class CompanyThingGroupTreeFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company',)
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')


class ConfigureAuthenticationSourceLDAP3Input(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('bind_dn', 'bind_password', 'company_id', 'email_attribute', 'encryption_method', 'host', 'is_active', 'name', 'name_attribute', 'phone_attribute', 'port', 'uid_attribute', 'user_search_base_dn', 'user_search_filter')
    bind_dn = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bindDN')
    bind_password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bindPassword')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='companyId')
    email_attribute = sgqlc.types.Field(String, graphql_name='emailAttribute')
    encryption_method = sgqlc.types.Field(sgqlc.types.non_null(LDAP3EncryptionMethod), graphql_name='encryptionMethod')
    host = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='host')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_attribute = sgqlc.types.Field(String, graphql_name='nameAttribute')
    phone_attribute = sgqlc.types.Field(String, graphql_name='phoneAttribute')
    port = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='port')
    uid_attribute = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uidAttribute')
    user_search_base_dn = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userSearchBaseDN')
    user_search_filter = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userSearchFilter')


class ConfigureAuthenticationSourceOAuth2Input(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('authorization_url', 'client_id', 'client_secret', 'company_id', 'email_attribute', 'is_active', 'name', 'name_attribute', 'phone_attribute', 'scope', 'token_url', 'uid_attribute', 'user_info_url')
    authorization_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='authorizationURL')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientID')
    client_secret = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientSecret')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='companyId')
    email_attribute = sgqlc.types.Field(String, graphql_name='emailAttribute')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_attribute = sgqlc.types.Field(String, graphql_name='nameAttribute')
    phone_attribute = sgqlc.types.Field(String, graphql_name='phoneAttribute')
    scope = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='scope')
    token_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenURL')
    uid_attribute = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uidAttribute')
    user_info_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userInfoURL')


class ConfigureAuthenticationSourceOpenIDConnect1Input(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('authorization_url', 'client_id', 'client_secret', 'company_id', 'configuration_method', 'configuration_url', 'email_attribute', 'is_active', 'jwks_url', 'name', 'name_attribute', 'phone_attribute', 'scope', 'token_url', 'uid_attribute')
    authorization_url = sgqlc.types.Field(String, graphql_name='authorizationURL')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientID')
    client_secret = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientSecret')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='companyId')
    configuration_method = sgqlc.types.Field(sgqlc.types.non_null(OpenIDConnect1ConfigurationMethod), graphql_name='configurationMethod')
    configuration_url = sgqlc.types.Field(String, graphql_name='configurationURL')
    email_attribute = sgqlc.types.Field(String, graphql_name='emailAttribute')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    jwks_url = sgqlc.types.Field(String, graphql_name='jwksURL')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_attribute = sgqlc.types.Field(String, graphql_name='nameAttribute')
    phone_attribute = sgqlc.types.Field(String, graphql_name='phoneAttribute')
    scope = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='scope')
    token_url = sgqlc.types.Field(String, graphql_name='tokenURL')
    uid_attribute = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uidAttribute')


class ConfigureAuthenticationSourceSAML2Input(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'is_active', 'name')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='companyId')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class ConfirmBorrowByThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('borrow_at', 'remark', 'thing', 'thing_borrow')
    borrow_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='borrowAt')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    thing = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='thing')
    thing_borrow = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='thingBorrow')


class ConfirmBorrowInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('borrow_at', 'id', 'remark')
    borrow_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='borrowAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class ConfirmReturnByThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('remark', 'return_at', 'thing')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    return_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='returnAt')
    thing = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='thing')


class ConfirmReturnInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'remark', 'return_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    return_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='returnAt')


class ConfirmSparePartClaimInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'item')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    item = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='item')


class ContentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('targets', 'template', 'url')
    targets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FieldInput'))), graphql_name='targets')
    template = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='template')
    url = sgqlc.types.Field(String, graphql_name='url')


class CountyFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('city',)
    city = sgqlc.types.Field('StringIDInput', graphql_name='city')


class CreateAccountInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account', 'is_allowed_to_login', 'password', 'roles', 'staff')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    is_allowed_to_login = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAllowedToLogin')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    roles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='roles')
    staff = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='staff')


class CreateAppVersionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app_id', 'description', 'version')
    app_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='appId')
    description = sgqlc.types.Field(String, graphql_name='description')
    version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='version')


class CreateCalibrateOrganizationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateCalibrateScheduleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'expire_day', 'generate_clock', 'generate_day', 'include_expired', 'is_all_department', 'is_all_thing_category', 'is_inside_calibrate', 'is_outside_calibrate', 'name', 'thing_category')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='department')
    expire_day = sgqlc.types.Field(Int, graphql_name='expireDay')
    generate_clock = sgqlc.types.Field(Int, graphql_name='generateClock')
    generate_day = sgqlc.types.Field(Int, graphql_name='generateDay')
    include_expired = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='includeExpired')
    is_all_department = sgqlc.types.Field(Boolean, graphql_name='isAllDepartment')
    is_all_thing_category = sgqlc.types.Field(Boolean, graphql_name='isAllThingCategory')
    is_inside_calibrate = sgqlc.types.Field(Boolean, graphql_name='isInsideCalibrate')
    is_outside_calibrate = sgqlc.types.Field(Boolean, graphql_name='isOutsideCalibrate')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='thingCategory')


class CreateChangeBorrowApproveConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'destination', 'source', 'trigger')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowState), graphql_name='destination')
    source = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowState), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowTrigger), graphql_name='trigger')


class CreateCompanyBIDatasourceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'datasource')
    company = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='company')
    datasource = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='datasource')


class CreateCompanyThingCategoryUCCFieldInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'data', 'name')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    data = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='data')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateDepositoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'factory', 'name')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    factory = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='factory')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateEamFileInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'file_name', 'length', 'name')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    file_name = sgqlc.types.Field(String, graphql_name='fileName')
    length = sgqlc.types.Field(Int, graphql_name='length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateEamSparePartCategoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name', 'parent_id')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(Int, graphql_name='parentId')


class CreateEamSparePartWarehouseInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateEnterpriseAppInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('description', 'name')
    description = sgqlc.types.Field(String, graphql_name='description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateEvasionDateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'end_date', 'name', 'start_date')
    company_id = sgqlc.types.Field(Int, graphql_name='companyId')
    end_date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endDate')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    start_date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startDate')


class CreateFactoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'name')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateFeaturePackInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('applicable_industries', 'name', 'remark')
    applicable_industries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='applicableIndustries')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class CreateFileInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('length', 'name')
    length = sgqlc.types.Field(Int, graphql_name='length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateImageInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('length', 'name')
    length = sgqlc.types.Field(Int, graphql_name='length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateInspectionMethodInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'field_data', 'name', 'thing_label')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='thingLabel')


class CreateMaintenanceMethodInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'field_data', 'name', 'thing_label')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='thingLabel')


class CreateMarketFileInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('length', 'name')
    length = sgqlc.types.Field(Int, graphql_name='length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateMetaTemplateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app', 'contents', 'description', 'event', 'fields', 'name', 'push_schedule', 'render_styles')
    app = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='app')
    contents = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ContentInput))), graphql_name='contents')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    event = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='event')
    fields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('FieldInput')), graphql_name='fields')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    push_schedule = sgqlc.types.Field('PushScheduleInput', graphql_name='pushSchedule')
    render_styles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RenderStyleInput'))), graphql_name='renderStyles')


class CreateOAuth2AuthenticationConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('access_token_attribute_path', 'account_attribute_path', 'authorization_url', 'client_authentication_method', 'client_id', 'client_secret', 'do_update_local_user_info_when_login', 'email_attribute_path', 'is_active', 'name', 'name_attribute_path', 'phone_number_attribute_path', 'scope', 'support_state', 'token_response_format', 'token_url', 'user_info_authentication_method', 'user_info_request_method', 'user_info_response_format', 'user_info_url')
    access_token_attribute_path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accessTokenAttributePath')
    account_attribute_path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accountAttributePath')
    authorization_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='authorizationUrl')
    client_authentication_method = sgqlc.types.Field(sgqlc.types.non_null(AuthenticationMethod), graphql_name='clientAuthenticationMethod')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')
    client_secret = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientSecret')
    do_update_local_user_info_when_login = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='doUpdateLocalUserInfoWhenLogin')
    email_attribute_path = sgqlc.types.Field(String, graphql_name='emailAttributePath')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_attribute_path = sgqlc.types.Field(String, graphql_name='nameAttributePath')
    phone_number_attribute_path = sgqlc.types.Field(String, graphql_name='phoneNumberAttributePath')
    scope = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='scope')
    support_state = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='supportState')
    token_response_format = sgqlc.types.Field(sgqlc.types.non_null(ResponseFormat), graphql_name='tokenResponseFormat')
    token_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenUrl')
    user_info_authentication_method = sgqlc.types.Field(sgqlc.types.non_null(AuthenticationMethod), graphql_name='userInfoAuthenticationMethod')
    user_info_request_method = sgqlc.types.Field(sgqlc.types.non_null(UserInfoRequestMethod), graphql_name='userInfoRequestMethod')
    user_info_response_format = sgqlc.types.Field(sgqlc.types.non_null(ResponseFormat), graphql_name='userInfoResponseFormat')
    user_info_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userInfoUrl')


class CreateOpenIDConnect1AuthenticationConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account_attribute_path', 'client_id', 'client_secret', 'configuration_url', 'do_update_local_user_info_when_login', 'email_attribute_path', 'is_active', 'kind', 'name', 'name_attribute_path', 'phone_number_attribute_path', 'scope')
    account_attribute_path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accountAttributePath')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')
    client_secret = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientSecret')
    configuration_url = sgqlc.types.Field(String, graphql_name='configurationUrl')
    do_update_local_user_info_when_login = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='doUpdateLocalUserInfoWhenLogin')
    email_attribute_path = sgqlc.types.Field(String, graphql_name='emailAttributePath')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    kind = sgqlc.types.Field(sgqlc.types.non_null(AuthenticationConfigurationKind), graphql_name='kind')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_attribute_path = sgqlc.types.Field(String, graphql_name='nameAttributePath')
    phone_number_attribute_path = sgqlc.types.Field(String, graphql_name='phoneNumberAttributePath')
    scope = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='scope')


class CreateOrganizationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'manager', 'name', 'parent')
    code = sgqlc.types.Field(String, graphql_name='code')
    manager = sgqlc.types.Field('StringIDInput', graphql_name='manager')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='parent')


class CreateOriginalInventoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('depository', 'inventory')
    depository = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='depository')
    inventory = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='inventory')


class CreateOutsideCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('apply_for_at', 'calibrate_at', 'calibrate_organization', 'company', 'name', 'pay_at', 'pay_status')
    apply_for_at = sgqlc.types.Field(Timestamp, graphql_name='applyForAt')
    calibrate_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='calibrateAt')
    calibrate_organization = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='calibrateOrganization')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pay_at = sgqlc.types.Field(Timestamp, graphql_name='payAt')
    pay_status = sgqlc.types.Field(OutsideCalibratePayStatus, graphql_name='payStatus')


class CreateRoleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('description', 'name')
    description = sgqlc.types.Field(String, graphql_name='description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateScheduleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end_at', 'estimated_time', 'inspection_method', 'maintenance_method', 'name', 'operator', 'repeat', 'start_at', 'ticket_type')
    end_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endAt')
    estimated_time = sgqlc.types.Field(String, graphql_name='estimatedTime')
    inspection_method = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='inspectionMethod')
    maintenance_method = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='maintenanceMethod')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    operator = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='operator')
    repeat = sgqlc.types.Field(sgqlc.types.non_null('RepeatInput'), graphql_name='repeat')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')
    ticket_type = sgqlc.types.Field(sgqlc.types.non_null(TicketType), graphql_name='ticketType')


class CreateSparePartClaimInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('date', 'department', 'item', 'reason', 'remark')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    department = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='department')
    item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SparePartClaimItemInput'))), graphql_name='item')
    reason = sgqlc.types.Field(sgqlc.types.non_null(SparePartClaimReason), graphql_name='reason')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class CreateSparePartInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'category', 'code', 'company', 'distributor', 'field_data', 'manufacturer', 'model', 'name', 'remark', 'safe_inventory_max', 'safe_inventory_min', 'specification')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='attachment')
    category = sgqlc.types.Field('IntIDInput', graphql_name='category')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field('IntIDInput', graphql_name='company')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    model = sgqlc.types.Field(String, graphql_name='model')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    safe_inventory_max = sgqlc.types.Field(Int, graphql_name='safeInventoryMax')
    safe_inventory_min = sgqlc.types.Field(Int, graphql_name='safeInventoryMin')
    specification = sgqlc.types.Field(String, graphql_name='specification')


class CreateSparePartOutboundInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('claim', 'date', 'item', 'kind', 'remark', 'warehouse')
    claim = sgqlc.types.Field('IntIDInput', graphql_name='claim')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CreateSparePartOutboundItemInput'))), graphql_name='item')
    kind = sgqlc.types.Field(sgqlc.types.non_null(SparePartOutboundKind), graphql_name='kind')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    warehouse = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='warehouse')


class CreateSparePartOutboundItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'spare_part')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='sparePart')


class CreateSparePartReceiptInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('date', 'item', 'kind', 'remark', 'warehouse')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CreateSparePartReceiptItemInput'))), graphql_name='item')
    kind = sgqlc.types.Field(sgqlc.types.non_null(SparePartReceiptKind), graphql_name='kind')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    warehouse = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='warehouse')


class CreateSparePartReceiptItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'spare_part')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='sparePart')


class CreateSparePartTransferInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('date', 'export', 'import_', 'item', 'remark')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    export = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='export')
    import_ = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='import')
    item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CreateSparePartTransferItemInput'))), graphql_name='item')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class CreateSparePartTransferItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'spare_part')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='sparePart')


class CreateSparePartUsageRecordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('record', 'spare_part_outbound')
    record = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SparePartUsageRecordInput'))), graphql_name='record')
    spare_part_outbound = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='sparePartOutbound')


class CreateSparePartWriteoffInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'issue', 'item', 'kind', 'reason')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    issue = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='issue')
    item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CreateSparePartWriteoffItemInput'))), graphql_name='item')
    kind = sgqlc.types.Field(sgqlc.types.non_null(SparePartWriteoffKind), graphql_name='kind')
    reason = sgqlc.types.Field(String, graphql_name='reason')


class CreateSparePartWriteoffItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('item', 'quantity')
    item = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='item')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')


class CreateStaffInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('avatar', 'email', 'job_number', 'job_status', 'job_type', 'name', 'organizations', 'phone_number', 'remark')
    avatar = sgqlc.types.Field('IDInput', graphql_name='avatar')
    email = sgqlc.types.Field(String, graphql_name='email')
    job_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='jobNumber')
    job_status = sgqlc.types.Field(sgqlc.types.non_null(StaffJobStatus), graphql_name='jobStatus')
    job_type = sgqlc.types.Field(sgqlc.types.non_null(StaffJobType), graphql_name='jobType')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    organizations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput'))), graphql_name='organizations')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class CreateTenantInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('address', 'city', 'code', 'county', 'email', 'industry', 'name', 'phone', 'province', 'type', 'uscc')
    address = sgqlc.types.Field(String, graphql_name='address')
    city = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='city')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    county = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='county')
    email = sgqlc.types.Field(String, graphql_name='email')
    industry = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='industry')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='province')
    type = sgqlc.types.Field(sgqlc.types.non_null(TenantType), graphql_name='type')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')


class CreateTenantOwnerInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account', 'email', 'name', 'password', 'phone_number', 'remark', 'tenant')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    email = sgqlc.types.Field(String, graphql_name='email')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    password = sgqlc.types.Field(String, graphql_name='password')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    tenant = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='tenant')


class CreateThingAdministratorDepartmentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('administrator', 'company', 'department')
    administrator = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='administrator')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    department = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='department')


class CreateThingAreaInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company', 'name', 'parent_id')
    code = sgqlc.types.Field(String, graphql_name='code')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(Int, graphql_name='parentId')


class CreateThingAttachmentTypeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateThingBarLabelInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('activate_bar_code', 'activate_field', 'activate_logo', 'bar_code_type', 'board_layout', 'company', 'field_key', 'font_size', 'height', 'logo', 'name', 'preview_image', 'show_bar_code', 'width')
    activate_bar_code = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='activateBarCode')
    activate_field = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='activateField')
    activate_logo = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='activateLogo')
    bar_code_type = sgqlc.types.Field(BarCodeType, graphql_name='barCodeType')
    board_layout = sgqlc.types.Field(JSON, graphql_name='boardLayout')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    field_key = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fieldKey')
    font_size = sgqlc.types.Field(Float, graphql_name='fontSize')
    height = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='height')
    logo = sgqlc.types.Field('StringIDInput', graphql_name='logo')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    preview_image = sgqlc.types.Field(String, graphql_name='previewImage')
    show_bar_code = sgqlc.types.Field(Boolean, graphql_name='showBarCode')
    width = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='width')


class CreateThingBorrowApproveConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'destination', 'source', 'trigger')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowState), graphql_name='destination')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowState), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowTrigger), graphql_name='trigger')


class CreateThingCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('reason', 'thing')
    reason = sgqlc.types.Field(sgqlc.types.non_null(CalibrateReason), graphql_name='reason')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='thing')


class CreateThingCalibrateOperatorInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'user')
    department = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='department')
    user = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='user')


class CreateThingCategoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company', 'name', 'parent_id')
    code = sgqlc.types.Field(String, graphql_name='code')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(Int, graphql_name='parentId')


class CreateThingCategoryUCCFieldInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('data', 'name', 'thing_category')
    data = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='data')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_category = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='thingCategory')


class CreateThingCompleteFileRuleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment_field', 'company', 'thing_category')
    attachment_field = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput'))), graphql_name='attachmentField')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    thing_category = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput'))), graphql_name='thingCategory')


class CreateThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company_id', 'name', 'parent')
    code = sgqlc.types.Field(String, graphql_name='code')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent = sgqlc.types.Field('IDInput', graphql_name='parent')


class CreateThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('acceptance_at', 'account_type', 'accounting_department', 'activated_at', 'alert_at', 'apply_for_purchase_at', 'apply_for_purchase_num', 'area', 'arrived_at', 'asset_normalization_at', 'attachment', 'book_value', 'brand', 'can_borrowed', 'category', 'code', 'code_prefix', 'company_id', 'contract_num', 'department', 'depreciation_of_year', 'depreciation_rate', 'depreciation_rate_of_month', 'desc', 'distributor', 'field_data', 'final_value', 'fuselage_code', 'group_file', 'image', 'installed_at', 'label', 'lease_begin_at', 'lease_finish_at', 'lease_num', 'machine_number', 'maintainer', 'manager', 'manufacturer', 'model_num', 'name', 'on_state', 'performance_status', 'po_num', 'predict_residual_rate', 'produce_at', 'purchase_price', 'purchase_type', 'purchased_at', 'sap_thing_code', 'serial_number', 'specification', 'storage_addr', 'storage_type', 'thing_group', 'thing_subject_code', 'transfer_at', 'used_year', 'warranty_deadline_at', 'warranty_institutions', 'warranty_method', 'years_of_use')
    acceptance_at = sgqlc.types.Field(Timestamp, graphql_name='acceptanceAt')
    account_type = sgqlc.types.Field(ThingAccountType, graphql_name='accountType')
    accounting_department = sgqlc.types.Field('IDInput', graphql_name='accountingDepartment')
    activated_at = sgqlc.types.Field(Timestamp, graphql_name='activatedAt')
    alert_at = sgqlc.types.Field(Timestamp, graphql_name='alertAt')
    apply_for_purchase_at = sgqlc.types.Field(Timestamp, graphql_name='applyForPurchaseAt')
    apply_for_purchase_num = sgqlc.types.Field(String, graphql_name='applyForPurchaseNum')
    area = sgqlc.types.Field('IntIDInput', graphql_name='area')
    arrived_at = sgqlc.types.Field(Timestamp, graphql_name='arrivedAt')
    asset_normalization_at = sgqlc.types.Field(Timestamp, graphql_name='assetNormalizationAt')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='attachment')
    book_value = sgqlc.types.Field(Float, graphql_name='bookValue')
    brand = sgqlc.types.Field(String, graphql_name='brand')
    can_borrowed = sgqlc.types.Field(Boolean, graphql_name='canBorrowed')
    category = sgqlc.types.Field('IntIDInput', graphql_name='category')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    code_prefix = sgqlc.types.Field(CodePrefix, graphql_name='codePrefix')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    contract_num = sgqlc.types.Field(String, graphql_name='contractNum')
    department = sgqlc.types.Field('IDInput', graphql_name='department')
    depreciation_of_year = sgqlc.types.Field(Float, graphql_name='depreciationOfYear')
    depreciation_rate = sgqlc.types.Field(Float, graphql_name='depreciationRate')
    depreciation_rate_of_month = sgqlc.types.Field(Float, graphql_name='depreciationRateOfMonth')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    final_value = sgqlc.types.Field(Float, graphql_name='finalValue')
    fuselage_code = sgqlc.types.Field(String, graphql_name='fuselageCode')
    group_file = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('GroupFileInput')), graphql_name='groupFile')
    image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='image')
    installed_at = sgqlc.types.Field(Timestamp, graphql_name='installedAt')
    label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='label')
    lease_begin_at = sgqlc.types.Field(Timestamp, graphql_name='leaseBeginAt')
    lease_finish_at = sgqlc.types.Field(Timestamp, graphql_name='leaseFinishAt')
    lease_num = sgqlc.types.Field(String, graphql_name='leaseNum')
    machine_number = sgqlc.types.Field(String, graphql_name='machineNumber')
    maintainer = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='maintainer')
    manager = sgqlc.types.Field('StringIDInput', graphql_name='manager')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    model_num = sgqlc.types.Field(String, graphql_name='modelNum')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    on_state = sgqlc.types.Field(OnState, graphql_name='onState')
    performance_status = sgqlc.types.Field(ThingPerformanceStatus, graphql_name='performanceStatus')
    po_num = sgqlc.types.Field(String, graphql_name='poNum')
    predict_residual_rate = sgqlc.types.Field(Float, graphql_name='predictResidualRate')
    produce_at = sgqlc.types.Field(Timestamp, graphql_name='produceAt')
    purchase_price = sgqlc.types.Field(Float, graphql_name='purchasePrice')
    purchase_type = sgqlc.types.Field(ThingPurchaseType, graphql_name='purchaseType')
    purchased_at = sgqlc.types.Field(Timestamp, graphql_name='purchasedAt')
    sap_thing_code = sgqlc.types.Field(String, graphql_name='sapThingCode')
    serial_number = sgqlc.types.Field(String, graphql_name='serialNumber')
    specification = sgqlc.types.Field(String, graphql_name='specification')
    storage_addr = sgqlc.types.Field(String, graphql_name='storageAddr')
    storage_type = sgqlc.types.Field(ThingStorageType, graphql_name='storageType')
    thing_group = sgqlc.types.Field('IDInput', graphql_name='thingGroup')
    thing_subject_code = sgqlc.types.Field(String, graphql_name='thingSubjectCode')
    transfer_at = sgqlc.types.Field(Timestamp, graphql_name='transferAt')
    used_year = sgqlc.types.Field(Float, graphql_name='usedYear')
    warranty_deadline_at = sgqlc.types.Field(Timestamp, graphql_name='warrantyDeadlineAt')
    warranty_institutions = sgqlc.types.Field(String, graphql_name='warrantyInstitutions')
    warranty_method = sgqlc.types.Field(ThingWarrantyMethod, graphql_name='warrantyMethod')
    years_of_use = sgqlc.types.Field(Float, graphql_name='yearsOfUse')


class CreateThingInspectionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'estimated_time', 'inspection_method', 'operator', 'thing')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    estimated_time = sgqlc.types.Field(String, graphql_name='estimatedTime')
    inspection_method = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput'))), graphql_name='inspectionMethod')
    operator = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='operator')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='thing')


class CreateThingInspectionWorkflowConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'destination', 'source', 'trigger')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionStatus), graphql_name='destination')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionStatus), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionTrigger), graphql_name='trigger')


class CreateThingInventoryRedundantRecordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('image', 'remark', 'ticket')
    image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='image')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    ticket = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='ticket')


class CreateThingInventoryTicketInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('constraint', 'method', 'name', 'plan_at', 'remark', 'thing_filter', 'user_scope')
    constraint = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInventoryConstraint)), graphql_name='constraint')
    method = sgqlc.types.Field(sgqlc.types.non_null(ThingInventoryMethod), graphql_name='method')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    plan_at = sgqlc.types.Field(sgqlc.types.non_null(TimestampRange), graphql_name='planAt')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    thing_filter = sgqlc.types.Field('ThingInventoryThingFilterInput', graphql_name='thingFilter')
    user_scope = sgqlc.types.Field(sgqlc.types.non_null(ThingInventoryUserScope), graphql_name='userScope')


class CreateThingLabelInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'name')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateThingMaintenanceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'estimated_time', 'maintenance_method', 'operator', 'thing')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    estimated_time = sgqlc.types.Field(String, graphql_name='estimatedTime')
    maintenance_method = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput'))), graphql_name='maintenanceMethod')
    operator = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='operator')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='thing')


class CreateThingMaintenanceWorkflowConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'destination', 'source', 'trigger')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceStatus), graphql_name='destination')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceStatus), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceTrigger), graphql_name='trigger')


class CreateThingRepairInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'estimated_time', 'found_at', 'operator', 'thing_repair_item')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    estimated_time = sgqlc.types.Field(String, graphql_name='estimatedTime')
    found_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='foundAt')
    operator = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='operator')
    thing_repair_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingRepairItemInput'))), graphql_name='thingRepairItem')


class CreateThingRepairWorkflowConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'destination', 'source', 'trigger')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairStatus), graphql_name='destination')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairStatus), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairTrigger), graphql_name='trigger')


class CreateThingScheduleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'schedule')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    schedule = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CreateScheduleInput))), graphql_name='schedule')


class CreateThingUCCInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name', 'thing_category')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='thingCategory')


class CreateUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account', 'email', 'is_account_enabled', 'name', 'organizations', 'password', 'phone_number', 'remark', 'roles')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    email = sgqlc.types.Field(String, graphql_name='email')
    is_account_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAccountEnabled')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    organizations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput'))), graphql_name='organizations')
    password = sgqlc.types.Field(String, graphql_name='password')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    roles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='roles')


class CurrentChangeBorrowApproveConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ChangeBorrowState)), graphql_name='source')


class CurrentThingBorrowApproveConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingBorrowState)), graphql_name='source')


class CurrentThingBorrowTransitionsFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'thing_borrow')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    thing_borrow = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='thingBorrow')


class CurrentThingInspectionWorkflowConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInspectionStatus)), graphql_name='source')


class CurrentThingMaintenanceWorkflowConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingMaintenanceStatus)), graphql_name='source')


class CurrentThingRepairWorkflowConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingRepairStatus)), graphql_name='source')


class DayOfYearInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('day', 'month')
    day = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='day')
    month = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='month')


class DeleteDepartmentThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'thing_groups')
    department = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='department')
    thing_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='thingGroups')


class DeleteThingBorrowDraftThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company', 'thing')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='thing')


class DeleteThingChangeBorrowDraftThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company', 'thing')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='thing')


class DepartmentListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company', 'current_only', 'ids', 'search')
    code = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='code')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    current_only = sgqlc.types.Field(Boolean, graphql_name='currentOnly')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='ids')
    search = sgqlc.types.Field(String, graphql_name='search')


class DepartmentThingAdministratorListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'user')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='department')
    user = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='user')


class DepartmentThingGroupFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'department')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='department')


class DepartmentTreeFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company',)
    company = sgqlc.types.Field('IDInput', graphql_name='company')


class DepositoryListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'factory_id', 'search')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    factory_id = sgqlc.types.Field(Int, graphql_name='factoryId')
    search = sgqlc.types.Field(String, graphql_name='search')


class DeptUserThingGroupInputFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('departments', 'search', 'user')
    departments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='departments')
    search = sgqlc.types.Field(String, graphql_name='search')
    user = sgqlc.types.Field('IDInput', graphql_name='user')


class DuplicateUCCFormStructureInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'key_pair')
    company = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='company')
    key_pair = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DuplicateUCCFormStructureKeyInput')), graphql_name='keyPair')


class DuplicateUCCFormStructureKeyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('new_key', 'old_key')
    new_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='newKey')
    old_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='oldKey')


class EamFieldInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment_type', 'company', 'content', 'default_bool', 'default_num', 'default_str', 'default_str_list', 'desc', 'extension', 'format', 'group', 'hint', 'id', 'is_active', 'max', 'max_count', 'max_range', 'max_size', 'min', 'min_range', 'multi', 'name', 'option', 'role', 'round', 'set', 'type', 'unit', 'zeroable')
    attachment_type = sgqlc.types.Field(EamAttachmentType, graphql_name='attachmentType')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    content = sgqlc.types.Field(String, graphql_name='content')
    default_bool = sgqlc.types.Field(Boolean, graphql_name='defaultBool')
    default_num = sgqlc.types.Field(Float, graphql_name='defaultNum')
    default_str = sgqlc.types.Field(String, graphql_name='defaultStr')
    default_str_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='defaultStrList')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    extension = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='extension')
    format = sgqlc.types.Field(String, graphql_name='format')
    group = sgqlc.types.Field(EamFieldGroupType, graphql_name='group')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(ID, graphql_name='id')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    max = sgqlc.types.Field(Float, graphql_name='max')
    max_count = sgqlc.types.Field(Int, graphql_name='maxCount')
    max_range = sgqlc.types.Field('EamMetaRangeExtremumInput', graphql_name='maxRange')
    max_size = sgqlc.types.Field(Int, graphql_name='maxSize')
    min = sgqlc.types.Field(Float, graphql_name='min')
    min_range = sgqlc.types.Field('EamMetaRangeExtremumInput', graphql_name='minRange')
    multi = sgqlc.types.Field(Boolean, graphql_name='multi')
    name = sgqlc.types.Field(String, graphql_name='name')
    option = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='option')
    role = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='role')
    round = sgqlc.types.Field(Int, graphql_name='round')
    set = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('EamFieldInput')), graphql_name='set')
    type = sgqlc.types.Field(sgqlc.types.non_null(EamFieldType), graphql_name='type')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    zeroable = sgqlc.types.Field(Boolean, graphql_name='zeroable')


class EamFieldInterListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('category', 'company', 'group', 'type')
    category = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='category')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    group = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EamFieldGroupType)), graphql_name='group')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EamFieldType)), graphql_name='type')


class EamFieldListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'exclude', 'form', 'group', 'is_active', 'name', 'search', 'search_by')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='exclude')
    form = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='form')
    group = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EamFieldGroupType)), graphql_name='group')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    name = sgqlc.types.Field(String, graphql_name='name')
    search = sgqlc.types.Field(String, graphql_name='search')
    search_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='searchBy')


class EamFileListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'file')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    file = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='file')


class EamFormByThingCategoryFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_category',)
    thing_category = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput'))), graphql_name='thingCategory')


class EamFormFieldInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('editable', 'field', 'option', 'required', 'width')
    editable = sgqlc.types.Field(Boolean, graphql_name='editable')
    field = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='field')
    option = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('EamFormFieldOptionInput')), graphql_name='option')
    required = sgqlc.types.Field(Boolean, graphql_name='required')
    width = sgqlc.types.Field(Int, graphql_name='width')


class EamFormFieldOptionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('field', 'option')
    field = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='field')
    option = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='option')


class EamFormFullFieldInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('editable', 'field', 'required', 'width')
    editable = sgqlc.types.Field(Boolean, graphql_name='editable')
    field = sgqlc.types.Field(sgqlc.types.non_null(EamFieldInput), graphql_name='field')
    required = sgqlc.types.Field(Boolean, graphql_name='required')
    width = sgqlc.types.Field(Int, graphql_name='width')


class EamFormListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company',)
    company = sgqlc.types.Field('IDInput', graphql_name='company')


class EamFormStructureFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    id = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='id')


class EamMetaRangeExtremumInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('default', 'hint', 'id', 'max', 'min', 'round', 'unit', 'zeroable')
    default = sgqlc.types.Field(Float, graphql_name='default')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(ID, graphql_name='id')
    max = sgqlc.types.Field(Float, graphql_name='max')
    min = sgqlc.types.Field(Float, graphql_name='min')
    round = sgqlc.types.Field(Int, graphql_name='round')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    zeroable = sgqlc.types.Field(Boolean, graphql_name='zeroable')


class EamSparePartCategoryListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'search')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')
    search = sgqlc.types.Field(String, graphql_name='search')


class EamSparePartFormStructureFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company',)
    company = sgqlc.types.Field('IDInput', graphql_name='company')


class EamSparePartWarehouseListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'manager', 'search')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    manager = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='manager')
    search = sgqlc.types.Field(String, graphql_name='search')


class EvasionDateFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')
    search = sgqlc.types.Field(String, graphql_name='search')


class ExcelFieldOption(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('label', 'value')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class ExcelTableFieldConfigInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('label', 'name', 'option', 'visible')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    option = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ExcelFieldOption)), graphql_name='option')
    visible = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='visible')


class ExportThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id')


class FactoryListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'search')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    search = sgqlc.types.Field(String, graphql_name='search')


class FeaturePackListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('industries', 'is_confirmed', 'search')
    industries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='industries')
    is_confirmed = sgqlc.types.Field(Boolean, graphql_name='isConfirmed')
    search = sgqlc.types.Field(String, graphql_name='search')


class FieldInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'description', 'example', 'is_target', 'name')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    description = sgqlc.types.Field(String, graphql_name='description')
    example = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='example')
    is_target = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTarget')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class GenerateCodeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('category_path_name', 'code_prefix', 'company', 'department_code', 'purchased_at')
    category_path_name = sgqlc.types.Field(String, graphql_name='categoryPathName')
    code_prefix = sgqlc.types.Field(String, graphql_name='codePrefix')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    department_code = sgqlc.types.Field(String, graphql_name='departmentCode')
    purchased_at = sgqlc.types.Field(Timestamp, graphql_name='purchasedAt')


class GroupFileInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('file', 'group_name')
    file = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='file')
    group_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='groupName')


class IDInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class InboxMessageFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('is_read', 'source_app_keys')
    is_read = sgqlc.types.Field(Boolean, graphql_name='isRead')
    source_app_keys = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sourceAppKeys')


class InspectionMethodListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search', 'thing_label')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')
    thing_label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='thingLabel')


class InspectionProcessItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'image', 'is_finished', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='image')
    is_finished = sgqlc.types.Field(Boolean, graphql_name='isFinished')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class IntIDInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class IsAttachmentTypeListExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsCalibrateOrganizationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(String, graphql_name='name')


class IsCalibrateScheduleExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsChangeBorrowApproveConfigurationExists(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source', 'trigger')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowState), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowTrigger), graphql_name='trigger')


class IsCompanyThingCategoryUCCFieldExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsDepositoryExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('factory_id', 'name')
    factory_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='factoryId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsEAMUCCFieldExistsFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'is_lock', 'name', 'type')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    is_lock = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLock')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(String, graphql_name='type')


class IsEamFieldExistsFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'is_lock', 'name', 'type')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    is_lock = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLock')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(String, graphql_name='type')


class IsEamFormExistsFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsEamSparePartCategoryExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name', 'parent_id')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(Int, graphql_name='parentId')


class IsEamSparePartWarehouseExistsFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsExistThingCirculationFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('state', 'thing')
    state = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BorrowState)), graphql_name='state')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')


class IsFactoryExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'name')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsInspectionMethodExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'name')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsMaintenanceMethodExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'name')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsOutsideCalibrateExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsSparePartExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company_id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')


class IsThingAreaCodeExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code',)
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')


class IsThingAreaExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name', 'parent_id')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(Int, graphql_name='parentId')


class IsThingBarLabelExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsThingBorrowApproveConfigurationExists(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source', 'trigger')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowState), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowTrigger), graphql_name='trigger')


class IsThingCategoryCodeExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')


class IsThingCategoryExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name', 'parent_id')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(Int, graphql_name='parentId')


class IsThingCategoryUCCFieldExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'thing_category')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_category = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='thingCategory')


class IsThingContainInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('category', 'company')
    category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='category')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')


class IsThingExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company_id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')


class IsThingInspectionWorkflowConfigurationExists(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source', 'trigger')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionStatus), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionTrigger), graphql_name='trigger')


class IsThingInventoryTicketExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsThingLabelExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'name')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsThingMaintenanceWorkflowConfigurationExists(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source', 'trigger')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceStatus), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceTrigger), graphql_name='trigger')


class IsThingRepairWorkflowConfigurationExists(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source', 'trigger')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairStatus), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairTrigger), graphql_name='trigger')


class IsThingScheduleExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsThingUCCExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IssueSparePartClaimInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('date', 'id', 'item', 'remark')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CreateSparePartOutboundItemInput))), graphql_name='item')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class LogListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('action', 'app_id', 'end', 'search', 'start')
    action = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(LogAction)), graphql_name='action')
    app_id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='appId')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    search = sgqlc.types.Field(String, graphql_name='search')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')


class LoginByEmailInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('email', 'new_password', 'password', 'verify_code')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    new_password = sgqlc.types.Field(String, graphql_name='newPassword')
    password = sgqlc.types.Field(String, graphql_name='password')
    verify_code = sgqlc.types.Field(String, graphql_name='verifyCode')


class LoginByPhoneNumberInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('phone_number', 'tenant_code', 'verify_code')
    phone_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phoneNumber')
    tenant_code = sgqlc.types.Field(String, graphql_name='tenantCode')
    verify_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='verifyCode')


class LoginInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account', 'password', 'tenant_code')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    tenant_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tenantCode')


class MaintenanceMethodListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search', 'thing_label')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')
    thing_label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingLabel')


class MaintenanceProcessItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'image', 'is_finished', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='image')
    is_finished = sgqlc.types.Field(Boolean, graphql_name='isFinished')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class MaintenanceSparePartItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'spare_part', 'spare_part_outbound')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='sparePart')
    spare_part_outbound = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='sparePartOutbound')


class MenuListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class MenuVisitHistoryListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class MessageTemplateListInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('available_channel_id', 'search')
    available_channel_id = sgqlc.types.Field(String, graphql_name='availableChannelId')
    search = sgqlc.types.Field(String, graphql_name='search')


class MetaTemplateListInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class MoveThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_group', 'things')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thingGroup')
    things = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='things')


class MyBacklogGroupFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('apps', 'groups', 'status')
    apps = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='apps')
    groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='groups')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BacklogStatus)), graphql_name='status')


class MyTenantAppListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('include_invisible', 'kinds', 'search')
    include_invisible = sgqlc.types.Field(Boolean, graphql_name='includeInvisible')
    kinds = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AppKind)), graphql_name='kinds')
    search = sgqlc.types.Field(String, graphql_name='search')


class MyTenantDevelopmentAppListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('include_not_online', 'search')
    include_not_online = sgqlc.types.Field(Boolean, graphql_name='includeNotOnline')
    search = sgqlc.types.Field(String, graphql_name='search')


class MyThingInventoryRecordListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'label', 'search', 'thing_area', 'thing_category', 'thing_inventory_state', 'thing_on_state', 'ticket')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='department')
    label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInventoryLabel)), graphql_name='label')
    search = sgqlc.types.Field(String, graphql_name='search')
    thing_area = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingArea')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingCategory')
    thing_inventory_state = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInventoryState)), graphql_name='thingInventoryState')
    thing_on_state = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(OnState)), graphql_name='thingOnState')
    ticket = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='ticket')


class OldRoleFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'permission', 'scope', 'search')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    id = sgqlc.types.Field(ID, graphql_name='id')
    permission = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='permission')
    scope = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='scope')
    search = sgqlc.types.Field(String, graphql_name='search')


class OperateSparePartClaimInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'operate_type', 'opinion')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operate_type = sgqlc.types.Field(sgqlc.types.non_null(SparePartClaimOperatorType), graphql_name='operateType')
    opinion = sgqlc.types.Field(String, graphql_name='opinion')


class OperateThingBorrowInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'id', 'operate_type', 'opinion')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='attachment')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operate_type = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowOperatorType), graphql_name='operateType')
    opinion = sgqlc.types.Field(String, graphql_name='opinion')


class OrganizationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_children_included', 'search')
    id = sgqlc.types.Field(String, graphql_name='id')
    is_children_included = sgqlc.types.Field(Boolean, graphql_name='isChildrenIncluded')
    search = sgqlc.types.Field(String, graphql_name='search')


class OrganizationTreeNodeFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class OutsideCalibrateListListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('calibrate_organization', 'company', 'search')
    calibrate_organization = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='calibrateOrganization')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')


class PageListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('apps', 'search')
    apps = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='apps')
    search = sgqlc.types.Field(String, graphql_name='search')


class PassThingInventoryRecordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'ticket')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')
    ticket = sgqlc.types.Field(IntIDInput, graphql_name='ticket')


class PauseThingMaintenanceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'lack_depository_name', 'lack_factory_name', 'lack_spare_part_names', 'pause_reason')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    lack_depository_name = sgqlc.types.Field(String, graphql_name='lackDepositoryName')
    lack_factory_name = sgqlc.types.Field(String, graphql_name='lackFactoryName')
    lack_spare_part_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lackSparePartNames')
    pause_reason = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pauseReason')


class PauseThingRepairInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'lack_depository_name', 'lack_factory_name', 'lack_spare_part_names', 'pause_reason')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    lack_depository_name = sgqlc.types.Field(String, graphql_name='lackDepositoryName')
    lack_factory_name = sgqlc.types.Field(String, graphql_name='lackFactoryName')
    lack_spare_part_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lackSparePartNames')
    pause_reason = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pauseReason')


class PermissionDataRangeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'name')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class PermissionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app_keys', 'exclude_app_keys', 'ids', 'is_leaf_only', 'require_data_ranges', 'search', 'types')
    app_keys = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='appKeys')
    exclude_app_keys = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='excludeAppKeys')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ids')
    is_leaf_only = sgqlc.types.Field(Boolean, graphql_name='isLeafOnly')
    require_data_ranges = sgqlc.types.Field(Boolean, graphql_name='requireDataRanges')
    search = sgqlc.types.Field(String, graphql_name='search')
    types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PermissionType)), graphql_name='types')


class PushScheduleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('type',)
    type = sgqlc.types.Field(PushScheduleType, graphql_name='type')


class RejectChangeBorrowInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'opinion')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    opinion = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='opinion')


class RejectTenantCertificationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'reason')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    reason = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reason')


class RejectThingCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'id', 'remark')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='attachment')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class RejectThingMaintenanceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class RejectThingRepairInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class RemoveAccountRolesInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account_ids', 'role_ids')
    account_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='accountIds')
    role_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='roleIds')


class RenderStyleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('config', 'kind', 'meta_channel_id')
    config = sgqlc.types.Field(JSON, graphql_name='config')
    kind = sgqlc.types.Field(MessageKind, graphql_name='kind')
    meta_channel_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='meta_channel_id')


class RepairSparePartItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'spare_part', 'spare_part_outbound')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='sparePart')
    spare_part_outbound = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='sparePartOutbound')


class RepeatInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('day_of_month', 'day_of_week', 'day_of_year', 'frequency', 'period')
    day_of_month = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dayOfMonth')
    day_of_week = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dayOfWeek')
    day_of_year = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DayOfYearInput)), graphql_name='dayOfYear')
    frequency = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='frequency')
    period = sgqlc.types.Field(sgqlc.types.non_null(RepeatPeriod), graphql_name='period')


class ReplaceThingBorrowInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'thing')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')


class ReplaceThingFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'id', 'search')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='department')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    search = sgqlc.types.Field(String, graphql_name='search')


class RestartThingInspectionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'operator', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='operator')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class RestartThingMaintenanceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'operator', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='operator')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class RestartThingRepairInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'operator', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='operator')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class RoleFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class RoleThingCategoryFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'role')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='role')


class SaveThingCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('calibrate_at', 'calibrate_label', 'calibrate_method', 'calibrate_organization', 'calibrate_report', 'calibrate_result', 'certificate_return_at', 'explain', 'id', 'return_at', 'send_at')
    calibrate_at = sgqlc.types.Field(Timestamp, graphql_name='calibrateAt')
    calibrate_label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='calibrateLabel')
    calibrate_method = sgqlc.types.Field(sgqlc.types.non_null(CalibrateMethod), graphql_name='calibrateMethod')
    calibrate_organization = sgqlc.types.Field(IDInput, graphql_name='calibrateOrganization')
    calibrate_report = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='calibrateReport')
    calibrate_result = sgqlc.types.Field(CalibrateResult, graphql_name='calibrateResult')
    certificate_return_at = sgqlc.types.Field(Timestamp, graphql_name='certificateReturnAt')
    explain = sgqlc.types.Field(String, graphql_name='explain')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    return_at = sgqlc.types.Field(Timestamp, graphql_name='returnAt')
    send_at = sgqlc.types.Field(Timestamp, graphql_name='sendAt')


class SaveThingInspectionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'related_operator', 'thing_inspection_process_item')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    related_operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='relatedOperator')
    thing_inspection_process_item = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingInspectionProcessItemInput')), graphql_name='thingInspectionProcessItem')


class SaveThingMaintenanceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'related_operator', 'thing_maintenance_process_item')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    related_operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='relatedOperator')
    thing_maintenance_process_item = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingMaintenanceProcessItemInput')), graphql_name='thingMaintenanceProcessItem')


class SaveThingRepairInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'related_operator', 'thing_repair_process_item')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    related_operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='relatedOperator')
    thing_repair_process_item = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingRepairProcessItemInput')), graphql_name='thingRepairProcessItem')


class SetAuthorizationRuleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('data_range', 'id', 'is_allowed', 'permission')
    data_range = sgqlc.types.Field(PermissionDataRangeInput, graphql_name='dataRange')
    id = sgqlc.types.Field(String, graphql_name='id')
    is_allowed = sgqlc.types.Field(Boolean, graphql_name='isAllowed')
    permission = sgqlc.types.Field('StringIDInput', graphql_name='permission')


class SetAuthorizationRulesToRoleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('authorization_rules', 'role')
    authorization_rules = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SetAuthorizationRuleInput))), graphql_name='authorizationRules')
    role = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='role')


class SetAuthorizationRulesToUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('authorization_rules', 'user')
    authorization_rules = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SetAuthorizationRuleInput))), graphql_name='authorizationRules')
    user = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='user')


class SetCodeRuleConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'configuration', 'rule')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    configuration = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CodeColumnConfigurationInput)), graphql_name='configuration')
    rule = sgqlc.types.Field(sgqlc.types.non_null(CodeRuleConfigurationRule), graphql_name='rule')


class SetCompanyThingDepartmentScope(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'scope')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    scope = sgqlc.types.Field(sgqlc.types.non_null(ThingDepartmentScope), graphql_name='scope')


class SetDepartmentThingGroup(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'thing_group')
    department = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='department')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thingGroup')


class SetDepartmentThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('departments', 'thing_group')
    departments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='departments')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thingGroup')


class SetEamFieldToEamFormInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('eam_field', 'eam_form')
    eam_field = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='eamField')
    eam_form = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput))), graphql_name='eamForm')


class SetEamFormStructureInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'name', 'zone')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    zone = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of(EamFormFieldInput)), graphql_name='zone')


class SetEamSparePartFormStructureInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'field', 'id')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    field = sgqlc.types.Field(sgqlc.types.list_of(EamFormFullFieldInput), graphql_name='field')
    id = sgqlc.types.Field(Int, graphql_name='id')


class SetEamSparePartWarehouseManager(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('manager', 'warehouse')
    manager = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='manager')
    warehouse = sgqlc.types.Field(IntIDInput, graphql_name='warehouse')


class SetFormThingCategoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('eam_form', 'option', 'thing_category')
    eam_form = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='eamForm')
    option = sgqlc.types.Field(SetOption, graphql_name='option')
    thing_category = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput))), graphql_name='thingCategory')


class SetLoginConfigToMyTenantInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('default_mode', 'modes')
    default_mode = sgqlc.types.Field(sgqlc.types.non_null(LoginMode), graphql_name='defaultMode')
    modes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LoginMode))), graphql_name='modes')


class SetLoginModesToTenantInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('modes', 'tenant')
    modes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LoginMode))), graphql_name='modes')
    tenant = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='tenant')


class SetOrganizationUsersInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('organization_id', 'staff_ids')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='organizationId')
    staff_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='staffIds')


class SetOutsideCalibrateThingCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('outside_calibrate', 'thing_calibrate')
    outside_calibrate = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='outsideCalibrate')
    thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thingCalibrate')


class SetPermissionToFeaturePackInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('feature_pack', 'permissions')
    feature_pack = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='featurePack')
    permissions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput'))), graphql_name='permissions')


class SetPermissionToTenantInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('permissions', 'tenant')
    permissions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput'))), graphql_name='permissions')
    tenant = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='tenant')


class SetRoleAccountInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account_ids', 'role_id')
    account_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='accountIds')
    role_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='roleId')


class SetRoleThingCategory(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('role', 'thing_category')
    role = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='role')
    thing_category = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput))), graphql_name='thingCategory')


class SetSingleDepartmentThingGroups(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'department_tree', 'thing_groups')
    department = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='department')
    department_tree = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='departmentTree')
    thing_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thingGroups')


class SetSingleUserThingGroupsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_groups', 'user')
    thing_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thingGroups')
    user = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='user')


class SetSparePartStockConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('role', 'scope')
    role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='role')
    scope = sgqlc.types.Field(sgqlc.types.non_null(SparePartStockScope), graphql_name='scope')


class SetSparePartThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('spare_part', 'thing')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='sparePart')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thing')


class SetSparePartWorkflowConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('under_confirm', 'under_issue', 'under_review')
    under_confirm = sgqlc.types.Field(sgqlc.types.non_null('SparePartSwitchInput'), graphql_name='underConfirm')
    under_issue = sgqlc.types.Field(sgqlc.types.non_null('SparePartSwitchInput'), graphql_name='underIssue')
    under_review = sgqlc.types.Field(sgqlc.types.non_null('SparePartReviewInput'), graphql_name='underReview')


class SetSubThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('sub_thing', 'thing')
    sub_thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='subThing')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')


class SetTableColumnSettingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('columns', 'key')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TableColumnInput'))), graphql_name='columns')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')


class SetTableFieldsConfigInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('fields', 'key')
    fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TableFieldConfigInput'))), graphql_name='fields')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')


class SetTableFixedFieldsConfigInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'fields', 'key')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TableFixedFieldInput'))), graphql_name='fields')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')


class SetThingBorrowInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'company', 'expected', 'id', 'reason', 'thing')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='attachment')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    expected = sgqlc.types.Field(TimestampRange, graphql_name='expected')
    id = sgqlc.types.Field(Int, graphql_name='id')
    reason = sgqlc.types.Field(String, graphql_name='reason')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thing')


class SetThingBorrowRangeConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'department', 'exclude', 'include', 'is_multiple', 'thing_category')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='department')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='exclude')
    include = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='include')
    is_multiple = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMultiple')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingCategory')


class SetThingBorrowWorkflowConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('borrow_evaluation', 'company', 'lost_confirmation', 'return_evaluation', 'under_review_by_apply_for', 'under_review_by_borrowed')
    borrow_evaluation = sgqlc.types.Field(sgqlc.types.non_null('ThingBorrowEvaluationInput'), graphql_name='borrowEvaluation')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    lost_confirmation = sgqlc.types.Field(sgqlc.types.non_null('ThingBorrowLostConfirmationInput'), graphql_name='lostConfirmation')
    return_evaluation = sgqlc.types.Field(sgqlc.types.non_null('ThingBorrowEvaluationInput'), graphql_name='returnEvaluation')
    under_review_by_apply_for = sgqlc.types.Field(sgqlc.types.non_null('ThingBorrowReviewInput'), graphql_name='underReviewByApplyFor')
    under_review_by_borrowed = sgqlc.types.Field(sgqlc.types.non_null('ThingBorrowReviewInput'), graphql_name='underReviewByBorrowed')


class SetThingCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('by_thing_repair', 'company')
    by_thing_repair = sgqlc.types.Field(Boolean, graphql_name='byThingRepair')
    company = sgqlc.types.Field(IDInput, graphql_name='company')


class SetThingCalibrateRangeConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_category',)
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingCategory')


class SetThingCalibrateWorkflowConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('pending', 'under_review')
    pending = sgqlc.types.Field(sgqlc.types.non_null('ThingCalibratePendingInput'), graphql_name='pending')
    under_review = sgqlc.types.Field(sgqlc.types.non_null('ThingCalibrateReviewInput'), graphql_name='underReview')


class SetThingDepartmentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'department')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    department = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='department')


class SetThingInventoryRecordByThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('image', 'label', 'remark', 'state', 'thing')
    image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='image')
    label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInventoryLabel)), graphql_name='label')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    state = sgqlc.types.Field(sgqlc.types.non_null(ThingInventoryState), graphql_name='state')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')


class SetThingInventoryRecordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'image', 'label', 'remark', 'state')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='image')
    label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInventoryLabel)), graphql_name='label')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    state = sgqlc.types.Field(sgqlc.types.non_null(ThingInventoryState), graphql_name='state')


class SetThingScheduleThing(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('schedule', 'thing')
    schedule = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput))), graphql_name='schedule')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thing')


class SetThingSparePartInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('spare_part', 'thing')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput))), graphql_name='sparePart')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')


class SetUCCFormStructureInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'key', 'zone')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    id = sgqlc.types.Field(ID, graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    zone = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of('UCCFieldInput')), graphql_name='zone')


class SetUCCStackDataInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'data', 'key')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    data = sgqlc.types.Field(JSON, graphql_name='data')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')


class SetUserThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_group', 'users')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thingGroup')
    users = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='users')


class SignUpCompanyTenantInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('city', 'code', 'contact', 'county', 'industry', 'name', 'phone', 'province', 'verify_code')
    city = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='city')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    contact = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='contact')
    county = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='county')
    industry = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='industry')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    phone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phone')
    province = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='province')
    verify_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='verifyCode')


class SparePartClaimItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'spare_part', 'warehouse')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='sparePart')
    warehouse = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='warehouse')


class SparePartClaimListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('created_by', 'department', 'id', 'reason', 'search', 'status', 'time_range', 'warehouse')
    created_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='createdBy')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='department')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')
    reason = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePartClaimReason)), graphql_name='reason')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePartClaimStatus)), graphql_name='status')
    time_range = sgqlc.types.Field(TimestampRange, graphql_name='timeRange')
    warehouse = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='warehouse')


class SparePartFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('category', 'company', 'exclude', 'id', 'only_unsafe_inventory', 'search', 'thing', 'warehouse')
    category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='category')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='exclude')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')
    only_unsafe_inventory = sgqlc.types.Field(Boolean, graphql_name='onlyUnsafeInventory')
    search = sgqlc.types.Field(String, graphql_name='search')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='thing')
    warehouse = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='warehouse')


class SparePartOutboundFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('claim', 'created_by', 'id', 'kind', 'search', 'time_range', 'warehouse')
    claim = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='claim')
    created_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='createdBy')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')
    kind = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePartOutboundKind)), graphql_name='kind')
    search = sgqlc.types.Field(String, graphql_name='search')
    time_range = sgqlc.types.Field(TimestampRange, graphql_name='timeRange')
    warehouse = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='warehouse')


class SparePartOutboundItemFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('spare_part_outbound',)
    spare_part_outbound = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='sparePartOutbound')


class SparePartOutboundSummaryFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_maintenance', 'thing_repair')
    thing_maintenance = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingMaintenance')
    thing_repair = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingRepair')


class SparePartReceiptFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('created_by', 'id', 'kind', 'search', 'time_range', 'warehouse')
    created_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='createdBy')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')
    kind = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePartReceiptKind)), graphql_name='kind')
    search = sgqlc.types.Field(String, graphql_name='search')
    time_range = sgqlc.types.Field(TimestampRange, graphql_name='timeRange')
    warehouse = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='warehouse')


class SparePartReceiptItemFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('receipt', 'search')
    receipt = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='receipt')
    search = sgqlc.types.Field(String, graphql_name='search')


class SparePartReceiptWriteoffFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('receipt',)
    receipt = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='receipt')


class SparePartReceiptWriteoffItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'spare_part')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='sparePart')


class SparePartReviewInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('assignee', 'default_review_operate', 'enabled', 'level')
    assignee = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='assignee')
    default_review_operate = sgqlc.types.Field(SparePartDefaultReviewOperate, graphql_name='defaultReviewOperate')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    level = sgqlc.types.Field(EamWorkflowReviewerLevel, graphql_name='level')


class SparePartStockFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('spare_part', 'warehouse')
    spare_part = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='sparePart')
    warehouse = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='warehouse')


class SparePartStockRecordFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('spare_part', 'type', 'warehouse')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='sparePart')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePartStockRecordType)), graphql_name='type')
    warehouse = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='warehouse')


class SparePartSwitchInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('enabled',)
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')


class SparePartTransferFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('created_by', 'export', 'id', 'import_', 'search', 'time_range')
    created_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='createdBy')
    export = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='export')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')
    import_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='import')
    search = sgqlc.types.Field(String, graphql_name='search')
    time_range = sgqlc.types.Field(TimestampRange, graphql_name='timeRange')


class SparePartTransferItemFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('transfer',)
    transfer = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='transfer')


class SparePartUsageRecordFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('claim', 'thing')
    claim = sgqlc.types.Field(IDInput, graphql_name='claim')
    thing = sgqlc.types.Field(IDInput, graphql_name='thing')


class SparePartUsageRecordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('spare_part', 'thing', 'usage_quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='sparePart')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')
    usage_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='usageQuantity')


class SparePartWriteoffFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_at', 'kind', 'search', 'start_at')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    kind = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePartWriteoffKind)), graphql_name='kind')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class StaffListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('include_children_organizations', 'job_status', 'job_type', 'organizations', 'search', 'search_by')
    include_children_organizations = sgqlc.types.Field(Boolean, graphql_name='includeChildrenOrganizations')
    job_status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StaffJobStatus)), graphql_name='jobStatus')
    job_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StaffJobType)), graphql_name='jobType')
    organizations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='organizations')
    search = sgqlc.types.Field(String, graphql_name='search')
    search_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='searchBy')


class StarAppInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app',)
    app = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='app')


class StringIDInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')


class SubThingListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing',)
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')


class SubThingUccListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'thing_category')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    thing_category = sgqlc.types.Field(IntIDInput, graphql_name='thingCategory')


class SystemLogFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('action', 'company', 'end', 'search', 'start')
    action = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='action')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')
    search = sgqlc.types.Field(String, graphql_name='search')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')


class TableColumnInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('disabled', 'fixed', 'name', 'unchecked')
    disabled = sgqlc.types.Field(Boolean, graphql_name='disabled')
    fixed = sgqlc.types.Field(Boolean, graphql_name='fixed')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    unchecked = sgqlc.types.Field(Boolean, graphql_name='unchecked')


class TableFieldConfigFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('disable_role_config', 'disable_user_config')
    disable_role_config = sgqlc.types.Field(Boolean, graphql_name='disableRoleConfig')
    disable_user_config = sgqlc.types.Field(Boolean, graphql_name='disableUserConfig')


class TableFieldConfigInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('editable', 'fixed', 'group', 'key', 'label', 'visible')
    editable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='editable')
    fixed = sgqlc.types.Field(Boolean, graphql_name='fixed')
    group = sgqlc.types.Field(TableFieldGroup, graphql_name='group')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    visible = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='visible')


class TableFixedFieldInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('disabled', 'hide', 'label', 'meta', 'name', 'options', 'required')
    disabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='disabled')
    hide = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hide')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    meta = sgqlc.types.Field(sgqlc.types.non_null('TableFixedFieldMetaInput'), graphql_name='meta')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    options = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TableFixedFieldOptionInput')), graphql_name='options')
    required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='required')


class TableFixedFieldMetaInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('can_config', 'can_disabled', 'can_hide', 'can_required', 'desc', 'group_name', 'label', 'options')
    can_config = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canConfig')
    can_disabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canDisabled')
    can_hide = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canHide')
    can_required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canRequired')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    group_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='groupName')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    options = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TableFixedFieldOptionInput')), graphql_name='options')


class TableFixedFieldOptionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('label', 'value')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class TableFixedFieldsConfigFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('can_config', 'company', 'group_name', 'hide', 'key', 'required', 'search')
    can_config = sgqlc.types.Field(Boolean, graphql_name='canConfig')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    group_name = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='groupName')
    hide = sgqlc.types.Field(Boolean, graphql_name='hide')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    required = sgqlc.types.Field(Boolean, graphql_name='required')
    search = sgqlc.types.Field(String, graphql_name='search')


class TenantAppListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'tenant')
    search = sgqlc.types.Field(String, graphql_name='search')
    tenant = sgqlc.types.Field(sgqlc.types.non_null(StringIDInput), graphql_name='tenant')


class TenantFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('certification_status', 'city_ids', 'county_ids', 'feature_packs', 'industry_ids', 'province_ids', 'search')
    certification_status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TenantCertificationStatus)), graphql_name='certificationStatus')
    city_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='cityIds')
    county_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='countyIds')
    feature_packs = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='featurePacks')
    industry_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='industryIds')
    province_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='provinceIds')
    search = sgqlc.types.Field(String, graphql_name='search')


class TenantIndustryTreeNodeFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class ThingAreaListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')
    search = sgqlc.types.Field(String, graphql_name='search')


class ThingAttachmentTypeListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company',)
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')


class ThingBarLabelListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company',)
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')


class ThingBorrowApproveConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingBorrowState)), graphql_name='source')


class ThingBorrowEvaluationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('assignee', 'default_review_operate', 'enabled', 'rule')
    assignee = sgqlc.types.Field(IDInput, graphql_name='assignee')
    default_review_operate = sgqlc.types.Field(EamWorkflowDefaultReviewOperate, graphql_name='defaultReviewOperate')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    rule = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingBorrowEvaluationRuleInput')), graphql_name='rule')


class ThingBorrowEvaluationRuleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('assignee', 'department', 'name', 'thing_category')
    assignee = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='assignee')
    department = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='department')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_category = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput))), graphql_name='thingCategory')


class ThingBorrowListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('applicant', 'company', 'department_of_applicant', 'department_of_manager', 'end_at', 'operator', 'search', 'start_at', 'state', 'status')
    applicant = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='applicant')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    department_of_applicant = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='departmentOfApplicant')
    department_of_manager = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='departmentOfManager')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='operator')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    state = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingBorrowState)), graphql_name='state')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingBorrowStatus)), graphql_name='status')


class ThingBorrowLostConfirmationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('enabled',)
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')


class ThingBorrowRelateResourceListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company',)
    company = sgqlc.types.Field(IDInput, graphql_name='company')


class ThingBorrowReviewInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('assignee', 'default_review_operate', 'enabled', 'level', 'reviewer')
    assignee = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='assignee')
    default_review_operate = sgqlc.types.Field(EamWorkflowDefaultReviewOperate, graphql_name='defaultReviewOperate')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    level = sgqlc.types.Field(EamWorkflowReviewerLevel, graphql_name='level')
    reviewer = sgqlc.types.Field(EamWorkflowReviewer, graphql_name='reviewer')


class ThingCalibrateListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('calibrate_organization', 'code', 'deadline', 'exclude_thing_calibrate', 'id', 'method', 'operator', 'reason', 'search', 'send_at', 'status', 'thing')
    calibrate_organization = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='calibrateOrganization')
    code = sgqlc.types.Field(String, graphql_name='code')
    deadline = sgqlc.types.Field(TimestampRange, graphql_name='deadline')
    exclude_thing_calibrate = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='excludeThingCalibrate')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id')
    method = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CalibrateMethod)), graphql_name='method')
    operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='operator')
    reason = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CalibrateReason)), graphql_name='reason')
    search = sgqlc.types.Field(String, graphql_name='search')
    send_at = sgqlc.types.Field(TimestampRange, graphql_name='sendAt')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingCalibrateStatus)), graphql_name='status')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')


class ThingCalibrateOperatorListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'user')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='department')
    user = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='user')


class ThingCalibratePendingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('assignee',)
    assignee = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='assignee')


class ThingCalibrateReviewInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('assignee', 'default_review_operate', 'level', 'reviewer')
    assignee = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='assignee')
    default_review_operate = sgqlc.types.Field(EamWorkflowDefaultReviewOperate, graphql_name='defaultReviewOperate')
    level = sgqlc.types.Field(EamWorkflowReviewerLevel, graphql_name='level')
    reviewer = sgqlc.types.Field(EamWorkflowReviewer, graphql_name='reviewer')


class ThingCategoryListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company', 'id', 'is_calibration', 'is_related_thing_complete_file_rule', 'is_related_thing_ucc', 'search', 'ucc_key')
    code = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='code')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')
    is_calibration = sgqlc.types.Field(Boolean, graphql_name='isCalibration')
    is_related_thing_complete_file_rule = sgqlc.types.Field(Boolean, graphql_name='isRelatedThingCompleteFileRule')
    is_related_thing_ucc = sgqlc.types.Field(Boolean, graphql_name='isRelatedThingUcc')
    search = sgqlc.types.Field(String, graphql_name='search')
    ucc_key = sgqlc.types.Field(String, graphql_name='uccKey')


class ThingCategoryUCCFieldListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'key', 'thing_category')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='key')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingCategory')


class ThingCirculationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('applicant', 'company', 'department', 'exclude_thing', 'is_lent', 'only_apply_for_department', 'only_manager', 'search', 'state', 'thing')
    applicant = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='applicant')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='department')
    exclude_thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='excludeThing')
    is_lent = sgqlc.types.Field(Boolean, graphql_name='isLent')
    only_apply_for_department = sgqlc.types.Field(Boolean, graphql_name='onlyApplyForDepartment')
    only_manager = sgqlc.types.Field(Boolean, graphql_name='onlyManager')
    search = sgqlc.types.Field(String, graphql_name='search')
    state = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BorrowState)), graphql_name='state')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')


class ThingCompleteFileRuleListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')


class ThingFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('calibrate_method', 'calibrate_result', 'calibrate_search', 'calibrate_state', 'can_borrowed', 'can_calibrate', 'company', 'current_only', 'department', 'department_order', 'exclude_thing', 'form', 'has_department', 'id', 'ids', 'include_deleted', 'include_sub_thing', 'is_calibration_expired', 'is_lent', 'label', 'manager', 'manager_order', 'next_calibrate_at', 'on_state', 'organization', 'qualified_parent', 'search', 'specification', 'thing_category', 'thing_group', 'ucc_key')
    calibrate_method = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CalibrateMethod)), graphql_name='calibrateMethod')
    calibrate_result = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CalibrateResult)), graphql_name='calibrateResult')
    calibrate_search = sgqlc.types.Field(String, graphql_name='calibrateSearch')
    calibrate_state = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CalibrateState)), graphql_name='calibrateState')
    can_borrowed = sgqlc.types.Field(Boolean, graphql_name='canBorrowed')
    can_calibrate = sgqlc.types.Field(Boolean, graphql_name='canCalibrate')
    company = sgqlc.types.Field(sgqlc.types.list_of(IDInput), graphql_name='company')
    current_only = sgqlc.types.Field(Boolean, graphql_name='currentOnly')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='department')
    department_order = sgqlc.types.Field(sgqlc.types.list_of(IDInput), graphql_name='departmentOrder')
    exclude_thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='excludeThing')
    form = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='form')
    has_department = sgqlc.types.Field(Boolean, graphql_name='hasDepartment')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids')
    include_deleted = sgqlc.types.Field(Boolean, graphql_name='includeDeleted')
    include_sub_thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='includeSubThing')
    is_calibration_expired = sgqlc.types.Field(Boolean, graphql_name='isCalibrationExpired')
    is_lent = sgqlc.types.Field(Boolean, graphql_name='isLent')
    label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='label')
    manager = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='manager')
    manager_order = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='managerOrder')
    next_calibrate_at = sgqlc.types.Field(TimestampRange, graphql_name='nextCalibrateAt')
    on_state = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(OnState)), graphql_name='onState')
    organization = sgqlc.types.Field(sgqlc.types.list_of(IDInput), graphql_name='organization')
    qualified_parent = sgqlc.types.Field(IDInput, graphql_name='qualifiedParent')
    search = sgqlc.types.Field(String, graphql_name='search')
    specification = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='specification')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingCategory')
    thing_group = sgqlc.types.Field(sgqlc.types.list_of(IDInput), graphql_name='thingGroup')
    ucc_key = sgqlc.types.Field(String, graphql_name='uccKey')


class ThingFunctionDepartmentFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'default_calibrate_user_search', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    default_calibrate_user_search = sgqlc.types.Field(String, graphql_name='defaultCalibrateUserSearch')
    search = sgqlc.types.Field(String, graphql_name='search')


class ThingGroupDeptFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('current_only', 'departments', 'thing_group')
    current_only = sgqlc.types.Field(Boolean, graphql_name='currentOnly')
    departments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='departments')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thingGroup')


class ThingGroupFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company', 'name')
    code = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='code')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    name = sgqlc.types.Field(String, graphql_name='name')


class ThingGroupUserFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('current_only', 'thing_group', 'users')
    current_only = sgqlc.types.Field(Boolean, graphql_name='currentOnly')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thingGroup')
    users = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='users')


class ThingInspectionListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_created_at', 'operator', 'search', 'start_created_at', 'status', 'thing')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    end_created_at = sgqlc.types.Field(Timestamp, graphql_name='endCreatedAt')
    operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='operator')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_created_at = sgqlc.types.Field(Timestamp, graphql_name='startCreatedAt')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInspectionStatus)), graphql_name='status')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')


class ThingInspectionProcessItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('inspection_process_item', 'thing')
    inspection_process_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InspectionProcessItemInput))), graphql_name='inspectionProcessItem')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')


class ThingInspectionWorkflowConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInspectionStatus)), graphql_name='source')


class ThingInventoryRecordListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('label', 'search', 'thing_category', 'thing_inventory_state', 'ticket')
    label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInventoryLabel)), graphql_name='label')
    search = sgqlc.types.Field(String, graphql_name='search')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingCategory')
    thing_inventory_state = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInventoryState)), graphql_name='thingInventoryState')
    ticket = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='ticket')


class ThingInventoryRedundantRecordListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ticket',)
    ticket = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='ticket')


class ThingInventoryThingFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'thing_category')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='department')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingCategory')


class ThingInventoryTicketListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('created_by', 'only_me', 'search', 'state', 'time_range')
    created_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='createdBy')
    only_me = sgqlc.types.Field(Boolean, graphql_name='onlyMe')
    search = sgqlc.types.Field(String, graphql_name='search')
    state = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInventoryTicketState)), graphql_name='state')
    time_range = sgqlc.types.Field(TimestampRange, graphql_name='timeRange')


class ThingInventoryTrackRecordListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ticket',)
    ticket = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='ticket')


class ThingInventoryTrackRedundantRecordListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ticket',)
    ticket = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='ticket')


class ThingLabelListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')


class ThingMaintenanceFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_at', 'end_created_at', 'operator', 'search', 'start_at', 'start_created_at', 'status', 'thing')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    end_created_at = sgqlc.types.Field(Timestamp, graphql_name='endCreatedAt')
    operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='operator')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    start_created_at = sgqlc.types.Field(Timestamp, graphql_name='startCreatedAt')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingMaintenanceStatus)), graphql_name='status')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')


class ThingMaintenanceProcessItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('maintenance_process_item', 'maintenance_spare_part_item', 'thing')
    maintenance_process_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MaintenanceProcessItemInput))), graphql_name='maintenanceProcessItem')
    maintenance_spare_part_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MaintenanceSparePartItemInput))), graphql_name='maintenanceSparePartItem')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')


class ThingMaintenanceWorkflowConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingMaintenanceStatus)), graphql_name='source')


class ThingRepairFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_created_at', 'operator', 'search', 'start_created_at', 'status', 'thing')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    end_created_at = sgqlc.types.Field(Timestamp, graphql_name='endCreatedAt')
    operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='operator')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_created_at = sgqlc.types.Field(Timestamp, graphql_name='startCreatedAt')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingRepairStatus)), graphql_name='status')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')


class ThingRepairItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('before_repair_image', 'repair_content', 'thing')
    before_repair_image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='beforeRepairImage')
    repair_content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repairContent')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')


class ThingRepairProcessItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('after_repair_image', 'id', 'remark', 'repair_spare_part_item', 'repair_type', 'thing')
    after_repair_image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='afterRepairImage')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    repair_spare_part_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RepairSparePartItemInput))), graphql_name='repairSparePartItem')
    repair_type = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairType), graphql_name='repairType')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')


class ThingRepairWorkflowConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingRepairStatus)), graphql_name='source')


class ThingScheduleFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'operator', 'search', 'thing', 'ticket_type')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='operator')
    search = sgqlc.types.Field(String, graphql_name='search')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')
    ticket_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TicketType)), graphql_name='ticketType')


class ThingTaskFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'execution_end_at', 'execution_start_at', 'operator', 'schedule', 'thing', 'ticket_type')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    execution_end_at = sgqlc.types.Field(Timestamp, graphql_name='executionEndAt')
    execution_start_at = sgqlc.types.Field(Timestamp, graphql_name='executionStartAt')
    operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='operator')
    schedule = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='schedule')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')
    ticket_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TicketType)), graphql_name='ticketType')


class ThingTransferRecordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('apply_for_at', 'field_data', 'group_file', 'process_id', 'sap_code_after_transfer', 'sap_code_before_transfer', 'transfer_in_department', 'transfer_out_department', 'transfer_type')
    apply_for_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='applyForAt')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    group_file = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GroupFileInput)), graphql_name='groupFile')
    process_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='processId')
    sap_code_after_transfer = sgqlc.types.Field(String, graphql_name='sapCodeAfterTransfer')
    sap_code_before_transfer = sgqlc.types.Field(String, graphql_name='sapCodeBeforeTransfer')
    transfer_in_department = sgqlc.types.Field(IDInput, graphql_name='transferInDepartment')
    transfer_out_department = sgqlc.types.Field(IDInput, graphql_name='transferOutDepartment')
    transfer_type = sgqlc.types.Field(sgqlc.types.non_null(ThingTransferType), graphql_name='transferType')


class ThingTransferRecordListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_apply_for_at', 'start_apply_for_at', 'thing', 'transfer_type')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    end_apply_for_at = sgqlc.types.Field(Timestamp, graphql_name='endApplyForAt')
    start_apply_for_at = sgqlc.types.Field(Timestamp, graphql_name='startApplyForAt')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')
    transfer_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingTransferType)), graphql_name='transferType')


class ThingUCCListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search', 'thing_category')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingCategory')


class TransferOrganizationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('origin_organization_id', 'staff_ids', 'target_organization_id')
    origin_organization_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='originOrganizationId')
    staff_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='staffIds')
    target_organization_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='targetOrganizationId')


class TurnToThingCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'id', 'operator', 'remark')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='attachment')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='operator')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class TurnToThingInspectionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'remark', 'turn_to')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    turn_to = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='turnTo')


class TurnToThingMaintenanceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'remark', 'turn_to')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    turn_to = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='turnTo')


class TurnToThingRepairInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'remark', 'turn_to')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    turn_to = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='turnTo')


class UCCFieldInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment_type', 'content', 'default_bool', 'default_num', 'default_str', 'default_str_list', 'extension', 'field_type', 'format', 'hint', 'id', 'label', 'max', 'max_count', 'max_range', 'max_size', 'min', 'min_range', 'multi', 'name', 'option', 'required', 'role', 'round', 'set', 'type', 'unit', 'width', 'zeroable')
    attachment_type = sgqlc.types.Field(UCCAttachmentType, graphql_name='attachmentType')
    content = sgqlc.types.Field(String, graphql_name='content')
    default_bool = sgqlc.types.Field(Boolean, graphql_name='defaultBool')
    default_num = sgqlc.types.Field(Float, graphql_name='defaultNum')
    default_str = sgqlc.types.Field(String, graphql_name='defaultStr')
    default_str_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='defaultStrList')
    extension = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='extension')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    format = sgqlc.types.Field(String, graphql_name='format')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(ID, graphql_name='id')
    label = sgqlc.types.Field(String, graphql_name='label')
    max = sgqlc.types.Field(Float, graphql_name='max')
    max_count = sgqlc.types.Field(Int, graphql_name='maxCount')
    max_range = sgqlc.types.Field('UCCMetaRangeExtremumInput', graphql_name='maxRange')
    max_size = sgqlc.types.Field(Int, graphql_name='maxSize')
    min = sgqlc.types.Field(Float, graphql_name='min')
    min_range = sgqlc.types.Field('UCCMetaRangeExtremumInput', graphql_name='minRange')
    multi = sgqlc.types.Field(Boolean, graphql_name='multi')
    name = sgqlc.types.Field(String, graphql_name='name')
    option = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='option')
    required = sgqlc.types.Field(Boolean, graphql_name='required')
    role = sgqlc.types.Field(sgqlc.types.list_of(IDInput), graphql_name='role')
    round = sgqlc.types.Field(Int, graphql_name='round')
    set = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UCCFieldInput')), graphql_name='set')
    type = sgqlc.types.Field(UCCFiledValue, graphql_name='type')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    width = sgqlc.types.Field(Int, graphql_name='width')
    zeroable = sgqlc.types.Field(Boolean, graphql_name='zeroable')


class UCCFormStructureFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'key', 'scope')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    scope = sgqlc.types.Field(UCCScope, graphql_name='scope')


class UCCMetaRangeExtremumInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('default', 'hint', 'max', 'min', 'required', 'unit', 'zeroable')
    default = sgqlc.types.Field(Float, graphql_name='default')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    max = sgqlc.types.Field(Float, graphql_name='max')
    min = sgqlc.types.Field(Float, graphql_name='min')
    required = sgqlc.types.Field(Boolean, graphql_name='required')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    zeroable = sgqlc.types.Field(Boolean, graphql_name='zeroable')


class UnAssignAppPermissionsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app', 'permissions')
    app = sgqlc.types.Field(sgqlc.types.non_null(StringIDInput), graphql_name='app')
    permissions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput))), graphql_name='permissions')


class UnAssignTenantAppsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('apps', 'tenant')
    apps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput))), graphql_name='apps')
    tenant = sgqlc.types.Field(sgqlc.types.non_null(StringIDInput), graphql_name='tenant')


class UnStarAppInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app',)
    app = sgqlc.types.Field(sgqlc.types.non_null(StringIDInput), graphql_name='app')


class UpdateAccountInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_allowed_to_login', 'roles')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    is_allowed_to_login = sgqlc.types.Field(Boolean, graphql_name='isAllowedToLogin')
    roles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='roles')


class UpdateAppVersionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('description', 'id', 'version')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    version = sgqlc.types.Field(String, graphql_name='version')


class UpdateAuthorizationRuleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('data_range', 'id', 'is_allowed')
    data_range = sgqlc.types.Field(PermissionDataRangeInput, graphql_name='dataRange')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    is_allowed = sgqlc.types.Field(Boolean, graphql_name='isAllowed')


class UpdateAuthorizationRulesOfUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('authorization_rules', 'user')
    authorization_rules = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UpdateAuthorizationRuleInput))), graphql_name='authorizationRules')
    user = sgqlc.types.Field(sgqlc.types.non_null(StringIDInput), graphql_name='user')


class UpdateCalibrateOrganizationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateCalibrateScheduleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'expire_day', 'generate_clock', 'generate_day', 'id', 'include_expired', 'is_all_department', 'is_all_thing_category', 'is_inside_calibrate', 'is_outside_calibrate', 'name', 'thing_category')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='department')
    expire_day = sgqlc.types.Field(Int, graphql_name='expireDay')
    generate_clock = sgqlc.types.Field(Int, graphql_name='generateClock')
    generate_day = sgqlc.types.Field(Int, graphql_name='generateDay')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    include_expired = sgqlc.types.Field(Boolean, graphql_name='includeExpired')
    is_all_department = sgqlc.types.Field(Boolean, graphql_name='isAllDepartment')
    is_all_thing_category = sgqlc.types.Field(Boolean, graphql_name='isAllThingCategory')
    is_inside_calibrate = sgqlc.types.Field(Boolean, graphql_name='isInsideCalibrate')
    is_outside_calibrate = sgqlc.types.Field(Boolean, graphql_name='isOutsideCalibrate')
    name = sgqlc.types.Field(String, graphql_name='name')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingCategory')


class UpdateChangeBorrowApproveConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(ChangeBorrowState, graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(ChangeBorrowState, graphql_name='source')
    trigger = sgqlc.types.Field(ChangeBorrowTrigger, graphql_name='trigger')


class UpdateCompanyThingCategoryUCCFieldInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('data', 'id', 'name')
    data = sgqlc.types.Field(JSON, graphql_name='data')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateDepartmentThingAdministratorInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('administrator', 'id')
    administrator = sgqlc.types.Field(IDInput, graphql_name='administrator')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')


class UpdateDepartmentThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'new_thing_group', 'old_thing_group')
    department = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='department')
    new_thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='newThingGroup')
    old_thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='oldThingGroup')


class UpdateDepositoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateEamFieldInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment_type', 'company', 'content', 'default_bool', 'default_num', 'default_str', 'default_str_list', 'desc', 'extension', 'format', 'group', 'hint', 'id', 'is_active', 'max', 'max_count', 'max_range', 'max_size', 'meta_id', 'min', 'min_range', 'multi', 'name', 'option', 'role', 'round', 'set', 'type', 'unit', 'zeroable')
    attachment_type = sgqlc.types.Field(EamAttachmentType, graphql_name='attachmentType')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    content = sgqlc.types.Field(String, graphql_name='content')
    default_bool = sgqlc.types.Field(Boolean, graphql_name='defaultBool')
    default_num = sgqlc.types.Field(Float, graphql_name='defaultNum')
    default_str = sgqlc.types.Field(String, graphql_name='defaultStr')
    default_str_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='defaultStrList')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    extension = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='extension')
    format = sgqlc.types.Field(String, graphql_name='format')
    group = sgqlc.types.Field(EamFieldGroupType, graphql_name='group')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    max = sgqlc.types.Field(Float, graphql_name='max')
    max_count = sgqlc.types.Field(Int, graphql_name='maxCount')
    max_range = sgqlc.types.Field(EamMetaRangeExtremumInput, graphql_name='maxRange')
    max_size = sgqlc.types.Field(Int, graphql_name='maxSize')
    meta_id = sgqlc.types.Field(ID, graphql_name='metaID')
    min = sgqlc.types.Field(Float, graphql_name='min')
    min_range = sgqlc.types.Field(EamMetaRangeExtremumInput, graphql_name='minRange')
    multi = sgqlc.types.Field(Boolean, graphql_name='multi')
    name = sgqlc.types.Field(String, graphql_name='name')
    option = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='option')
    role = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='role')
    round = sgqlc.types.Field(Int, graphql_name='round')
    set = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EamFieldInput)), graphql_name='set')
    type = sgqlc.types.Field(EamFieldType, graphql_name='type')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    zeroable = sgqlc.types.Field(Boolean, graphql_name='zeroable')


class UpdateEamSparePartCategoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateEamSparePartWarehouseInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateEnterpriseAppInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('avatar', 'description', 'group', 'id', 'name', 'redirect_url', 'url')
    avatar = sgqlc.types.Field(IDInput, graphql_name='avatar')
    description = sgqlc.types.Field(String, graphql_name='description')
    group = sgqlc.types.Field(StringIDInput, graphql_name='group')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    redirect_url = sgqlc.types.Field(String, graphql_name='redirectUrl')
    url = sgqlc.types.Field(String, graphql_name='url')


class UpdateEvasionDateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end_date', 'id', 'name', 'start_date')
    end_date = sgqlc.types.Field(Timestamp, graphql_name='endDate')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    start_date = sgqlc.types.Field(Timestamp, graphql_name='startDate')


class UpdateFactoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateFeaturePackInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('applicable_industries', 'id', 'name', 'remark')
    applicable_industries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='applicableIndustries')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class UpdateInspectionMethodInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('field_data', 'id', 'name', 'thing_label')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    thing_label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingLabel')


class UpdateMaintenanceMethodInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('field_data', 'id', 'name', 'thing_label')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    thing_label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingLabel')


class UpdateMeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('avatar', 'email', 'name', 'phone_number')
    avatar = sgqlc.types.Field(IDInput, graphql_name='avatar')
    email = sgqlc.types.Field(String, graphql_name='email')
    name = sgqlc.types.Field(String, graphql_name='name')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')


class UpdateMetaChannelInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('description', 'id')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')


class UpdateMetaTemplateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('contents', 'description', 'event', 'fields', 'id', 'name', 'push_schedule', 'render_styles', 'status', 'tenant_id')
    contents = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ContentInput)), graphql_name='contents')
    description = sgqlc.types.Field(String, graphql_name='description')
    event = sgqlc.types.Field(String, graphql_name='event')
    fields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldInput)), graphql_name='fields')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    push_schedule = sgqlc.types.Field(PushScheduleInput, graphql_name='pushSchedule')
    render_styles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RenderStyleInput)), graphql_name='renderStyles')
    status = sgqlc.types.Field(sgqlc.types.non_null(TemplateStatus), graphql_name='status')
    tenant_id = sgqlc.types.Field(String, graphql_name='tenantId')


class UpdateOAuth2AuthenticationConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('access_token_attribute_path', 'account_attribute_path', 'authorization_url', 'client_authentication_method', 'client_id', 'client_secret', 'do_update_local_user_info_when_login', 'email_attribute_path', 'id', 'is_active', 'name', 'name_attribute_path', 'phone_number_attribute_path', 'scope', 'support_state', 'token_response_format', 'token_url', 'user_info_authentication_method', 'user_info_request_method', 'user_info_response_format', 'user_info_url')
    access_token_attribute_path = sgqlc.types.Field(String, graphql_name='accessTokenAttributePath')
    account_attribute_path = sgqlc.types.Field(String, graphql_name='accountAttributePath')
    authorization_url = sgqlc.types.Field(String, graphql_name='authorizationUrl')
    client_authentication_method = sgqlc.types.Field(AuthenticationMethod, graphql_name='clientAuthenticationMethod')
    client_id = sgqlc.types.Field(String, graphql_name='clientId')
    client_secret = sgqlc.types.Field(String, graphql_name='clientSecret')
    do_update_local_user_info_when_login = sgqlc.types.Field(Boolean, graphql_name='doUpdateLocalUserInfoWhenLogin')
    email_attribute_path = sgqlc.types.Field(String, graphql_name='emailAttributePath')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_attribute_path = sgqlc.types.Field(String, graphql_name='nameAttributePath')
    phone_number_attribute_path = sgqlc.types.Field(String, graphql_name='phoneNumberAttributePath')
    scope = sgqlc.types.Field(String, graphql_name='scope')
    support_state = sgqlc.types.Field(Boolean, graphql_name='supportState')
    token_response_format = sgqlc.types.Field(ResponseFormat, graphql_name='tokenResponseFormat')
    token_url = sgqlc.types.Field(String, graphql_name='tokenUrl')
    user_info_authentication_method = sgqlc.types.Field(AuthenticationMethod, graphql_name='userInfoAuthenticationMethod')
    user_info_request_method = sgqlc.types.Field(UserInfoRequestMethod, graphql_name='userInfoRequestMethod')
    user_info_response_format = sgqlc.types.Field(ResponseFormat, graphql_name='userInfoResponseFormat')
    user_info_url = sgqlc.types.Field(String, graphql_name='userInfoUrl')


class UpdateOpenIDConnect1AuthenticationConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account_attribute_path', 'client_id', 'client_secret', 'configuration_url', 'do_update_local_user_info_when_login', 'email_attribute_path', 'id', 'is_active', 'name', 'name_attribute_path', 'phone_number_attribute_path', 'scope')
    account_attribute_path = sgqlc.types.Field(String, graphql_name='accountAttributePath')
    client_id = sgqlc.types.Field(String, graphql_name='clientId')
    client_secret = sgqlc.types.Field(String, graphql_name='clientSecret')
    configuration_url = sgqlc.types.Field(String, graphql_name='configurationUrl')
    do_update_local_user_info_when_login = sgqlc.types.Field(Boolean, graphql_name='doUpdateLocalUserInfoWhenLogin')
    email_attribute_path = sgqlc.types.Field(String, graphql_name='emailAttributePath')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_attribute_path = sgqlc.types.Field(String, graphql_name='nameAttributePath')
    phone_number_attribute_path = sgqlc.types.Field(String, graphql_name='phoneNumberAttributePath')
    scope = sgqlc.types.Field(String, graphql_name='scope')


class UpdateOrganizationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'id', 'manager', 'name')
    code = sgqlc.types.Field(String, graphql_name='code')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    manager = sgqlc.types.Field(StringIDInput, graphql_name='manager')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateOutsideCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('apply_for_at', 'calibrate_at', 'id', 'name', 'pay_at', 'pay_status')
    apply_for_at = sgqlc.types.Field(Timestamp, graphql_name='applyForAt')
    calibrate_at = sgqlc.types.Field(Timestamp, graphql_name='calibrateAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    pay_at = sgqlc.types.Field(Timestamp, graphql_name='payAt')
    pay_status = sgqlc.types.Field(OutsideCalibratePayStatus, graphql_name='payStatus')


class UpdateRoleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('description', 'id', 'name')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateSparePartClaimInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('date', 'department', 'id', 'item', 'reason', 'remark')
    date = sgqlc.types.Field(Timestamp, graphql_name='date')
    department = sgqlc.types.Field(IDInput, graphql_name='department')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    item = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePartClaimItemInput)), graphql_name='item')
    reason = sgqlc.types.Field(SparePartClaimReason, graphql_name='reason')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class UpdateSparePartInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'category', 'distributor', 'field_data', 'id', 'manufacturer', 'model', 'name', 'remark', 'safe_inventory_max', 'safe_inventory_min', 'specification')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='attachment')
    category = sgqlc.types.Field(IntIDInput, graphql_name='category')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    model = sgqlc.types.Field(String, graphql_name='model')
    name = sgqlc.types.Field(String, graphql_name='name')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    safe_inventory_max = sgqlc.types.Field(Int, graphql_name='safeInventoryMax')
    safe_inventory_min = sgqlc.types.Field(Int, graphql_name='safeInventoryMin')
    specification = sgqlc.types.Field(String, graphql_name='specification')


class UpdateStaffInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('avatar', 'email', 'id', 'job_number', 'job_status', 'job_type', 'name', 'organizations', 'phone_number', 'remark')
    avatar = sgqlc.types.Field(IDInput, graphql_name='avatar')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    job_number = sgqlc.types.Field(String, graphql_name='jobNumber')
    job_status = sgqlc.types.Field(StaffJobStatus, graphql_name='jobStatus')
    job_type = sgqlc.types.Field(StaffJobType, graphql_name='jobType')
    name = sgqlc.types.Field(String, graphql_name='name')
    organizations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='organizations')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class UpdateTenantInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('address', 'business_license_image', 'city', 'code', 'county', 'email', 'id', 'industry', 'name', 'phone', 'province', 'uscc')
    address = sgqlc.types.Field(String, graphql_name='address')
    business_license_image = sgqlc.types.Field(IDInput, graphql_name='businessLicenseImage')
    city = sgqlc.types.Field(StringIDInput, graphql_name='city')
    code = sgqlc.types.Field(String, graphql_name='code')
    county = sgqlc.types.Field(StringIDInput, graphql_name='county')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    industry = sgqlc.types.Field(StringIDInput, graphql_name='industry')
    name = sgqlc.types.Field(String, graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(StringIDInput, graphql_name='province')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')


class UpdateThingAreaInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'id', 'name')
    code = sgqlc.types.Field(String, graphql_name='code')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateThingAttachmentTypeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'next_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    next_id = sgqlc.types.Field(Int, graphql_name='nextId')


class UpdateThingBarLabelInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('activate_bar_code', 'activate_field', 'activate_logo', 'bar_code_type', 'board_layout', 'field_key', 'font_size', 'height', 'id', 'logo', 'name', 'preview_image', 'show_bar_code', 'width')
    activate_bar_code = sgqlc.types.Field(Boolean, graphql_name='activateBarCode')
    activate_field = sgqlc.types.Field(Boolean, graphql_name='activateField')
    activate_logo = sgqlc.types.Field(Boolean, graphql_name='activateLogo')
    bar_code_type = sgqlc.types.Field(BarCodeType, graphql_name='barCodeType')
    board_layout = sgqlc.types.Field(JSON, graphql_name='boardLayout')
    field_key = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fieldKey')
    font_size = sgqlc.types.Field(Float, graphql_name='fontSize')
    height = sgqlc.types.Field(Int, graphql_name='height')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    logo = sgqlc.types.Field(StringIDInput, graphql_name='logo')
    name = sgqlc.types.Field(String, graphql_name='name')
    preview_image = sgqlc.types.Field(String, graphql_name='previewImage')
    show_bar_code = sgqlc.types.Field(Boolean, graphql_name='showBarCode')
    width = sgqlc.types.Field(Int, graphql_name='width')


class UpdateThingBorrowApproveConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(ThingBorrowState, graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(ThingBorrowState, graphql_name='source')
    trigger = sgqlc.types.Field(ThingBorrowTrigger, graphql_name='trigger')


class UpdateThingBorrowDraftThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company', 'expected_borrow_at', 'expected_return_at', 'thing')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    expected_borrow_at = sgqlc.types.Field(Timestamp, graphql_name='expectedBorrowAt')
    expected_return_at = sgqlc.types.Field(Timestamp, graphql_name='expectedReturnAt')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thing')


class UpdateThingBorrowInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'company', 'expected', 'id', 'reason', 'thing')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='attachment')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    expected = sgqlc.types.Field(TimestampRange, graphql_name='expected')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    reason = sgqlc.types.Field(String, graphql_name='reason')
    thing = sgqlc.types.Field(IDInput, graphql_name='thing')


class UpdateThingByCodeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('acceptance_at', 'account_type', 'accounting_department', 'activated_at', 'alert_at', 'apply_for_purchase_at', 'apply_for_purchase_num', 'area', 'arrived_at', 'asset_normalization_at', 'attachment', 'book_value', 'brand', 'calibrate_code', 'calibrate_method', 'calibrate_repeat', 'can_borrowed', 'category', 'code', 'contract_num', 'department', 'depreciation_of_year', 'depreciation_rate', 'depreciation_rate_of_month', 'desc', 'distributor', 'field_data', 'final_value', 'fuselage_code', 'group_file', 'image', 'installed_at', 'label', 'lease_begin_at', 'lease_finish_at', 'lease_num', 'machine_number', 'maintainer', 'manager', 'manufacturer', 'name', 'on_state', 'performance_status', 'po_num', 'predict_residual_rate', 'produce_at', 'purchase_price', 'purchase_type', 'purchased_at', 'sap_thing_code', 'serial_number', 'specification', 'storage_addr', 'storage_type', 'thing_group', 'thing_subject_code', 'transfer_at', 'used_year', 'warranty_deadline_at', 'warranty_institutions', 'warranty_method', 'years_of_use')
    acceptance_at = sgqlc.types.Field(Timestamp, graphql_name='acceptanceAt')
    account_type = sgqlc.types.Field(ThingAccountType, graphql_name='accountType')
    accounting_department = sgqlc.types.Field(IDInput, graphql_name='accountingDepartment')
    activated_at = sgqlc.types.Field(Timestamp, graphql_name='activatedAt')
    alert_at = sgqlc.types.Field(Timestamp, graphql_name='alertAt')
    apply_for_purchase_at = sgqlc.types.Field(Timestamp, graphql_name='applyForPurchaseAt')
    apply_for_purchase_num = sgqlc.types.Field(String, graphql_name='applyForPurchaseNum')
    area = sgqlc.types.Field(IntIDInput, graphql_name='area')
    arrived_at = sgqlc.types.Field(Timestamp, graphql_name='arrivedAt')
    asset_normalization_at = sgqlc.types.Field(Timestamp, graphql_name='assetNormalizationAt')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='attachment')
    book_value = sgqlc.types.Field(Float, graphql_name='bookValue')
    brand = sgqlc.types.Field(String, graphql_name='brand')
    calibrate_code = sgqlc.types.Field(String, graphql_name='calibrateCode')
    calibrate_method = sgqlc.types.Field(CalibrateMethod, graphql_name='calibrateMethod')
    calibrate_repeat = sgqlc.types.Field(CalibrateRepeatInput, graphql_name='calibrateRepeat')
    can_borrowed = sgqlc.types.Field(Boolean, graphql_name='canBorrowed')
    category = sgqlc.types.Field(IntIDInput, graphql_name='category')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    contract_num = sgqlc.types.Field(String, graphql_name='contractNum')
    department = sgqlc.types.Field(IDInput, graphql_name='department')
    depreciation_of_year = sgqlc.types.Field(Int, graphql_name='depreciationOfYear')
    depreciation_rate = sgqlc.types.Field(Float, graphql_name='depreciationRate')
    depreciation_rate_of_month = sgqlc.types.Field(Float, graphql_name='depreciationRateOfMonth')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    final_value = sgqlc.types.Field(Float, graphql_name='finalValue')
    fuselage_code = sgqlc.types.Field(String, graphql_name='fuselageCode')
    group_file = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GroupFileInput)), graphql_name='groupFile')
    image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='image')
    installed_at = sgqlc.types.Field(Timestamp, graphql_name='installedAt')
    label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='label')
    lease_begin_at = sgqlc.types.Field(Timestamp, graphql_name='leaseBeginAt')
    lease_finish_at = sgqlc.types.Field(Timestamp, graphql_name='leaseFinishAt')
    lease_num = sgqlc.types.Field(String, graphql_name='leaseNum')
    machine_number = sgqlc.types.Field(String, graphql_name='machineNumber')
    maintainer = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='maintainer')
    manager = sgqlc.types.Field(StringIDInput, graphql_name='manager')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    name = sgqlc.types.Field(String, graphql_name='name')
    on_state = sgqlc.types.Field(OnState, graphql_name='onState')
    performance_status = sgqlc.types.Field(ThingPerformanceStatus, graphql_name='performanceStatus')
    po_num = sgqlc.types.Field(String, graphql_name='poNum')
    predict_residual_rate = sgqlc.types.Field(Float, graphql_name='predictResidualRate')
    produce_at = sgqlc.types.Field(Timestamp, graphql_name='produceAt')
    purchase_price = sgqlc.types.Field(Float, graphql_name='purchasePrice')
    purchase_type = sgqlc.types.Field(ThingPurchaseType, graphql_name='purchaseType')
    purchased_at = sgqlc.types.Field(Timestamp, graphql_name='purchasedAt')
    sap_thing_code = sgqlc.types.Field(String, graphql_name='sapThingCode')
    serial_number = sgqlc.types.Field(String, graphql_name='serialNumber')
    specification = sgqlc.types.Field(String, graphql_name='specification')
    storage_addr = sgqlc.types.Field(String, graphql_name='storageAddr')
    storage_type = sgqlc.types.Field(ThingStorageType, graphql_name='storageType')
    thing_group = sgqlc.types.Field(IDInput, graphql_name='thingGroup')
    thing_subject_code = sgqlc.types.Field(String, graphql_name='thingSubjectCode')
    transfer_at = sgqlc.types.Field(Timestamp, graphql_name='transferAt')
    used_year = sgqlc.types.Field(Float, graphql_name='usedYear')
    warranty_deadline_at = sgqlc.types.Field(Timestamp, graphql_name='warrantyDeadlineAt')
    warranty_institutions = sgqlc.types.Field(String, graphql_name='warrantyInstitutions')
    warranty_method = sgqlc.types.Field(ThingWarrantyMethod, graphql_name='warrantyMethod')
    years_of_use = sgqlc.types.Field(Float, graphql_name='yearsOfUse')


class UpdateThingCalibrateOperatorInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'user')
    department = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='department')
    user = sgqlc.types.Field(sgqlc.types.non_null(StringIDInput), graphql_name='user')


class UpdateThingCategoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'id', 'name')
    code = sgqlc.types.Field(String, graphql_name='code')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateThingCategoryUCCFieldInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('data', 'id', 'name')
    data = sgqlc.types.Field(JSON, graphql_name='data')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateThingChangeBorrowDraftThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('change_return_at', 'code', 'company', 'thing')
    change_return_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='changeReturnAt')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thing')


class UpdateThingCompleteFileRuleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment_field', 'id', 'thing_category')
    attachment_field = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput))), graphql_name='attachmentField')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingCategory')


class UpdateThingFunctionDepartmentsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('default_calibrate_user', 'id')
    default_calibrate_user = sgqlc.types.Field(IDInput, graphql_name='defaultCalibrateUser')
    id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id')


class UpdateThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'id', 'name', 'parent')
    code = sgqlc.types.Field(String, graphql_name='code')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    parent = sgqlc.types.Field(IDInput, graphql_name='parent')


class UpdateThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('acceptance_at', 'account_type', 'accounting_department', 'activated_at', 'alert_at', 'apply_for_purchase_at', 'apply_for_purchase_num', 'area', 'arrived_at', 'asset_normalization_at', 'attachment', 'book_value', 'brand', 'calibrate_code', 'calibrate_method', 'calibrate_repeat', 'can_borrowed', 'category', 'code_prefix', 'contract_num', 'department', 'depreciation_of_year', 'depreciation_rate', 'depreciation_rate_of_month', 'desc', 'distributor', 'field_data', 'final_value', 'fuselage_code', 'group_file', 'id', 'image', 'installed_at', 'label', 'lease_begin_at', 'lease_finish_at', 'lease_num', 'machine_number', 'maintainer', 'manager', 'manufacturer', 'model_num', 'name', 'on_state', 'performance_status', 'po_num', 'predict_residual_rate', 'produce_at', 'purchase_price', 'purchase_type', 'purchased_at', 'sap_thing_code', 'serial_number', 'specification', 'storage_addr', 'storage_type', 'thing_group', 'thing_subject_code', 'transfer_at', 'used_year', 'warranty_deadline_at', 'warranty_institutions', 'warranty_method', 'years_of_use')
    acceptance_at = sgqlc.types.Field(Timestamp, graphql_name='acceptanceAt')
    account_type = sgqlc.types.Field(ThingAccountType, graphql_name='accountType')
    accounting_department = sgqlc.types.Field(IDInput, graphql_name='accountingDepartment')
    activated_at = sgqlc.types.Field(Timestamp, graphql_name='activatedAt')
    alert_at = sgqlc.types.Field(Timestamp, graphql_name='alertAt')
    apply_for_purchase_at = sgqlc.types.Field(Timestamp, graphql_name='applyForPurchaseAt')
    apply_for_purchase_num = sgqlc.types.Field(String, graphql_name='applyForPurchaseNum')
    area = sgqlc.types.Field(IntIDInput, graphql_name='area')
    arrived_at = sgqlc.types.Field(Timestamp, graphql_name='arrivedAt')
    asset_normalization_at = sgqlc.types.Field(Timestamp, graphql_name='assetNormalizationAt')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='attachment')
    book_value = sgqlc.types.Field(Float, graphql_name='bookValue')
    brand = sgqlc.types.Field(String, graphql_name='brand')
    calibrate_code = sgqlc.types.Field(String, graphql_name='calibrateCode')
    calibrate_method = sgqlc.types.Field(CalibrateMethod, graphql_name='calibrateMethod')
    calibrate_repeat = sgqlc.types.Field(CalibrateRepeatInput, graphql_name='calibrateRepeat')
    can_borrowed = sgqlc.types.Field(Boolean, graphql_name='canBorrowed')
    category = sgqlc.types.Field(IntIDInput, graphql_name='category')
    code_prefix = sgqlc.types.Field(CodePrefix, graphql_name='codePrefix')
    contract_num = sgqlc.types.Field(String, graphql_name='contractNum')
    department = sgqlc.types.Field(IDInput, graphql_name='department')
    depreciation_of_year = sgqlc.types.Field(Float, graphql_name='depreciationOfYear')
    depreciation_rate = sgqlc.types.Field(Float, graphql_name='depreciationRate')
    depreciation_rate_of_month = sgqlc.types.Field(Float, graphql_name='depreciationRateOfMonth')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    final_value = sgqlc.types.Field(Float, graphql_name='finalValue')
    fuselage_code = sgqlc.types.Field(String, graphql_name='fuselageCode')
    group_file = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GroupFileInput)), graphql_name='groupFile')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='image')
    installed_at = sgqlc.types.Field(Timestamp, graphql_name='installedAt')
    label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='label')
    lease_begin_at = sgqlc.types.Field(Timestamp, graphql_name='leaseBeginAt')
    lease_finish_at = sgqlc.types.Field(Timestamp, graphql_name='leaseFinishAt')
    lease_num = sgqlc.types.Field(String, graphql_name='leaseNum')
    machine_number = sgqlc.types.Field(String, graphql_name='machineNumber')
    maintainer = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='maintainer')
    manager = sgqlc.types.Field(StringIDInput, graphql_name='manager')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    model_num = sgqlc.types.Field(String, graphql_name='modelNum')
    name = sgqlc.types.Field(String, graphql_name='name')
    on_state = sgqlc.types.Field(OnState, graphql_name='onState')
    performance_status = sgqlc.types.Field(ThingPerformanceStatus, graphql_name='performanceStatus')
    po_num = sgqlc.types.Field(String, graphql_name='poNum')
    predict_residual_rate = sgqlc.types.Field(Float, graphql_name='predictResidualRate')
    produce_at = sgqlc.types.Field(Timestamp, graphql_name='produceAt')
    purchase_price = sgqlc.types.Field(Float, graphql_name='purchasePrice')
    purchase_type = sgqlc.types.Field(ThingPurchaseType, graphql_name='purchaseType')
    purchased_at = sgqlc.types.Field(Timestamp, graphql_name='purchasedAt')
    sap_thing_code = sgqlc.types.Field(String, graphql_name='sapThingCode')
    serial_number = sgqlc.types.Field(String, graphql_name='serialNumber')
    specification = sgqlc.types.Field(String, graphql_name='specification')
    storage_addr = sgqlc.types.Field(String, graphql_name='storageAddr')
    storage_type = sgqlc.types.Field(ThingStorageType, graphql_name='storageType')
    thing_group = sgqlc.types.Field(IDInput, graphql_name='thingGroup')
    thing_subject_code = sgqlc.types.Field(String, graphql_name='thingSubjectCode')
    transfer_at = sgqlc.types.Field(Timestamp, graphql_name='transferAt')
    used_year = sgqlc.types.Field(Float, graphql_name='usedYear')
    warranty_deadline_at = sgqlc.types.Field(Timestamp, graphql_name='warrantyDeadlineAt')
    warranty_institutions = sgqlc.types.Field(String, graphql_name='warrantyInstitutions')
    warranty_method = sgqlc.types.Field(ThingWarrantyMethod, graphql_name='warrantyMethod')
    years_of_use = sgqlc.types.Field(Float, graphql_name='yearsOfUse')


class UpdateThingInspectionWorkflowConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(ThingInspectionStatus, graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(ThingInspectionStatus, graphql_name='source')
    trigger = sgqlc.types.Field(ThingInspectionTrigger, graphql_name='trigger')


class UpdateThingInventoryRedundantRecordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'image', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='image')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class UpdateThingLabelInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateThingMaintenanceWorkflowConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(ThingMaintenanceStatus, graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(ThingMaintenanceStatus, graphql_name='source')
    trigger = sgqlc.types.Field(ThingMaintenanceTrigger, graphql_name='trigger')


class UpdateThingRepairWorkflowConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(ThingRepairStatus, graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(ThingRepairStatus, graphql_name='source')
    trigger = sgqlc.types.Field(ThingRepairTrigger, graphql_name='trigger')


class UpdateThingScheduleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end_at', 'estimated_time', 'id', 'inspection_method', 'maintenance_method', 'name', 'operator', 'repeat', 'start_at')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    estimated_time = sgqlc.types.Field(String, graphql_name='estimatedTime')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    inspection_method = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='inspectionMethod')
    maintenance_method = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='maintenanceMethod')
    name = sgqlc.types.Field(String, graphql_name='name')
    operator = sgqlc.types.Field(IDInput, graphql_name='operator')
    repeat = sgqlc.types.Field(RepeatInput, graphql_name='repeat')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class UpdateThingTaskInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('execution_at', 'id', 'operator')
    execution_at = sgqlc.types.Field(Timestamp, graphql_name='executionAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(IDInput, graphql_name='operator')


class UpdateThingUCCInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'thing_category')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingCategory')


class UpdateThingsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('calibrate_method', 'calibrate_repeat', 'id')
    calibrate_method = sgqlc.types.Field(CalibrateMethod, graphql_name='calibrateMethod')
    calibrate_repeat = sgqlc.types.Field(CalibrateRepeatInput, graphql_name='calibrateRepeat')
    id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id')


class UpdateUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('email', 'id', 'is_account_enabled', 'name', 'organizations', 'phone_number', 'remark', 'roles')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    is_account_enabled = sgqlc.types.Field(Boolean, graphql_name='isAccountEnabled')
    name = sgqlc.types.Field(String, graphql_name='name')
    organizations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='organizations')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    roles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='roles')


class UpdateUserThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('new_thing_group', 'old_thing_group')
    new_thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='newThingGroup')
    old_thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='oldThingGroup')


class UpdateWorkflowBaseConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('change_borrow_init_state', 'change_borrow_use_default_workflow', 'company', 'thing_borrow_init_state', 'thing_borrow_use_default_workflow', 'thing_calibrate_init_state', 'thing_calibrate_use_default_workflow', 'thing_inspection_init_state', 'thing_inspection_use_default_workflow', 'thing_maintenance_init_state', 'thing_maintenance_use_default_workflow', 'thing_repair_init_state', 'thing_repair_use_default_workflow')
    change_borrow_init_state = sgqlc.types.Field(ChangeBorrowState, graphql_name='changeBorrowInitState')
    change_borrow_use_default_workflow = sgqlc.types.Field(Boolean, graphql_name='changeBorrowUseDefaultWorkflow')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    thing_borrow_init_state = sgqlc.types.Field(ThingBorrowState, graphql_name='thingBorrowInitState')
    thing_borrow_use_default_workflow = sgqlc.types.Field(Boolean, graphql_name='thingBorrowUseDefaultWorkflow')
    thing_calibrate_init_state = sgqlc.types.Field(ThingCalibrateState, graphql_name='thingCalibrateInitState')
    thing_calibrate_use_default_workflow = sgqlc.types.Field(Boolean, graphql_name='thingCalibrateUseDefaultWorkflow')
    thing_inspection_init_state = sgqlc.types.Field(ThingInspectionStatus, graphql_name='thingInspectionInitState')
    thing_inspection_use_default_workflow = sgqlc.types.Field(Boolean, graphql_name='thingInspectionUseDefaultWorkflow')
    thing_maintenance_init_state = sgqlc.types.Field(ThingMaintenanceStatus, graphql_name='thingMaintenanceInitState')
    thing_maintenance_use_default_workflow = sgqlc.types.Field(Boolean, graphql_name='thingMaintenanceUseDefaultWorkflow')
    thing_repair_init_state = sgqlc.types.Field(ThingRepairStatus, graphql_name='thingRepairInitState')
    thing_repair_use_default_workflow = sgqlc.types.Field(Boolean, graphql_name='thingRepairUseDefaultWorkflow')


class UseSparePartClaimInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'item')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    item = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UseSparePartClaimItemInput')), graphql_name='item')


class UseSparePartClaimItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('spare_part', 'used_thing')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='sparePart')
    used_thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UsedSparePartClaimThingInput')), graphql_name='usedThing')


class UsedSparePartClaimThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'thing')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')


class UserFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('accounts', 'include_children_organizations', 'include_disabled_users', 'is_account_enabled', 'is_admin', 'organizations', 'roles', 'search', 'search_by')
    accounts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='accounts')
    include_children_organizations = sgqlc.types.Field(Boolean, graphql_name='includeChildrenOrganizations')
    include_disabled_users = sgqlc.types.Field(Boolean, graphql_name='includeDisabledUsers')
    is_account_enabled = sgqlc.types.Field(Boolean, graphql_name='isAccountEnabled')
    is_admin = sgqlc.types.Field(Boolean, graphql_name='isAdmin')
    organizations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='organizations')
    roles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='roles')
    search = sgqlc.types.Field(String, graphql_name='search')
    search_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='searchBy')


class UserListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'current_only', 'department', 'ids', 'is_active', 'role', 'search', 'search_name', 'uid')
    company = sgqlc.types.Field(IntIDInput, graphql_name='company')
    current_only = sgqlc.types.Field(Boolean, graphql_name='currentOnly')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='department')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='ids')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='role')
    search = sgqlc.types.Field(String, graphql_name='search')
    search_name = sgqlc.types.Field(String, graphql_name='searchName')
    uid = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='uid')


class WriteoffSparePartReceiptInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'item', 'reason')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartReceiptWriteoffItemInput))), graphql_name='item')
    reason = sgqlc.types.Field(String, graphql_name='reason')


class countryFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('full',)
    full = sgqlc.types.Field(Boolean, graphql_name='full')


class uccStackDataFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'key')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')



########################################################################
# Output Objects and Interfaces
########################################################################
class Account(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('account', 'email', 'id', 'is_admin', 'is_allowed_to_login', 'is_email_verified', 'is_owner', 'is_phone_number_verified', 'phone_number', 'roles', 'staff', 'wecom_user')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    is_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAdmin')
    is_allowed_to_login = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAllowedToLogin')
    is_email_verified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEmailVerified')
    is_owner = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isOwner')
    is_phone_number_verified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPhoneNumberVerified')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    roles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Role'))), graphql_name='roles')
    staff = sgqlc.types.Field(sgqlc.types.non_null('Staff'), graphql_name='staff')
    wecom_user = sgqlc.types.Field('WecomUser', graphql_name='wecomUser')


class AccountList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Account))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Api(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('doc_url', 'id', 'name', 'permission_id', 'url')
    doc_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='docUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    permission_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='permissionId')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class App(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('avatar', 'client_id', 'client_secret', 'code', 'description', 'dispatched_permissions', 'group', 'id', 'jump_kind', 'kind', 'name', 'online_version', 'order', 'redirect_url', 'url', 'versions')
    avatar = sgqlc.types.Field('Image', graphql_name='avatar')
    client_id = sgqlc.types.Field(String, graphql_name='clientId')
    client_secret = sgqlc.types.Field(String, graphql_name='clientSecret')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    description = sgqlc.types.Field(String, graphql_name='description')
    dispatched_permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Permission')), graphql_name='dispatchedPermissions')
    group = sgqlc.types.Field(sgqlc.types.non_null('AppGroup'), graphql_name='group')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    jump_kind = sgqlc.types.Field(sgqlc.types.non_null(JumpKind), graphql_name='jumpKind')
    kind = sgqlc.types.Field(sgqlc.types.non_null(AppKind), graphql_name='kind')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    online_version = sgqlc.types.Field('AppVersion', graphql_name='onlineVersion')
    order = sgqlc.types.Field(Float, graphql_name='order')
    redirect_url = sgqlc.types.Field(String, graphql_name='redirectUrl')
    url = sgqlc.types.Field(String, graphql_name='url')
    versions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('AppVersion')), graphql_name='versions')


class AppBIDatasourceList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app', 'datasource')
    app = sgqlc.types.Field(App, graphql_name='app')
    datasource = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BIDatasource'))), graphql_name='datasource')


class AppGroup(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app_ids', 'id', 'name')
    app_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='appIds')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class AppList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(App))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AppMenu(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app', 'menus')
    app = sgqlc.types.Field(App, graphql_name='app')
    menus = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Menu'))), graphql_name='menus')


class AppMenuList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AppMenu))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AppVersion(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app_id', 'description', 'difference', 'id', 'snapshot', 'status', 'version')
    app_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='appId')
    description = sgqlc.types.Field(String, graphql_name='description')
    difference = sgqlc.types.Field('AppVersionDifference', graphql_name='difference')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    snapshot = sgqlc.types.Field('AppVersionSnapshot', graphql_name='snapshot')
    status = sgqlc.types.Field(sgqlc.types.non_null(AppVersionStatus), graphql_name='status')
    version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='version')


class AppVersionDifference(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('perm_diffs',)
    perm_diffs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AppVersionPermDiff'))), graphql_name='permDiffs')


class AppVersionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AppVersion))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AppVersionPermDiff(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('category', 'permission')
    category = sgqlc.types.Field(DifferenceResult, graphql_name='category')
    permission = sgqlc.types.Field(sgqlc.types.non_null('Permission'), graphql_name='permission')


class AppVersionSnapshot(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('perm_snapshot',)
    perm_snapshot = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Permission'))), graphql_name='permSnapshot')


class AuthInfo(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('token', 'user_id')
    token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='token')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')


class AuthenticationConfiguration(sgqlc.types.Interface):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_active', 'kind', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    kind = sgqlc.types.Field(sgqlc.types.non_null(AuthenticationConfigurationKind), graphql_name='kind')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class AuthenticationSource(sgqlc.types.Interface):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_active', 'kind', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    kind = sgqlc.types.Field(sgqlc.types.non_null(AuthenticationSourceKind), graphql_name='kind')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Authorization(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data_ranges', 'is_allowed', 'is_expired', 'permission')
    data_ranges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='dataRanges')
    is_allowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAllowed')
    is_expired = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isExpired')
    permission = sgqlc.types.Field(sgqlc.types.non_null('Permission'), graphql_name='permission')


class AuthorizationRule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data_range', 'id', 'is_allowed', 'permission')
    data_range = sgqlc.types.Field('PermissionDataRange', graphql_name='dataRange')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    is_allowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAllowed')
    permission = sgqlc.types.Field(sgqlc.types.non_null('Permission'), graphql_name='permission')


class AuthorizationRuleDependentBy(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('dependencies', 'id')
    dependencies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AuthorizationRule)), graphql_name='dependencies')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')


class AuthorizationRuleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AuthorizationRule))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class BIDatasource(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'id', 'name', 'used')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    used = sgqlc.types.Field(Boolean, graphql_name='used')


class BIResult(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('metric', 'timestamp', 'value')
    metric = sgqlc.types.Field(String, graphql_name='metric')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')
    value = sgqlc.types.Field(Float, graphql_name='value')


class Backlog(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('created_at', 'data', 'group_id', 'id', 'status', 'title', 'updated_at', 'url')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BacklogFieldData')), graphql_name='data')
    group_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='groupId')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    status = sgqlc.types.Field(sgqlc.types.non_null(BacklogStatus), graphql_name='status')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class BacklogFieldData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class BacklogFieldMeta(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('key', 'style')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    style = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='style')


class BacklogGroup(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app', 'fields', 'id', 'name')
    app = sgqlc.types.Field(sgqlc.types.non_null(App), graphql_name='app')
    fields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BacklogFieldMeta)), graphql_name='fields')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CalibrateOrganization(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CalibrateOrganizationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CalibrateOrganization))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CalibrateRepeat(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('frequency', 'period')
    frequency = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='frequency')
    period = sgqlc.types.Field(sgqlc.types.non_null(CalibrateRepeatPeriod), graphql_name='period')


class CalibrateSchedule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('created_at', 'department', 'expire_day', 'generate_clock', 'generate_day', 'id', 'include_expired', 'is_all_department', 'is_all_thing_category', 'is_inside_calibrate', 'is_outside_calibrate', 'name', 'thing_category', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Department')), graphql_name='department')
    expire_day = sgqlc.types.Field(Int, graphql_name='expireDay')
    generate_clock = sgqlc.types.Field(Int, graphql_name='generateClock')
    generate_day = sgqlc.types.Field(Int, graphql_name='generateDay')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    include_expired = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='includeExpired')
    is_all_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAllDepartment')
    is_all_thing_category = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAllThingCategory')
    is_inside_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isInsideCalibrate')
    is_outside_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isOutsideCalibrate')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingCategory')), graphql_name='thingCategory')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class CalibrateScheduleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CalibrateSchedule))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CalibrateScheduleRepeat(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('day_of_month',)
    day_of_month = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='dayOfMonth')


class ChangeBorrow(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('applicant', 'code', 'created_at', 'department_of_applicant', 'department_of_manager', 'id', 'reason', 'state', 'updated_at')
    applicant = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='applicant')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    department_of_applicant = sgqlc.types.Field(sgqlc.types.non_null('Department'), graphql_name='departmentOfApplicant')
    department_of_manager = sgqlc.types.Field(sgqlc.types.non_null('Department'), graphql_name='departmentOfManager')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    reason = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reason')
    state = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowState), graphql_name='state')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class ChangeBorrowApproveConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowState), graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowState), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowTrigger), graphql_name='trigger')


class ChangeBorrowApproveConfigurationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ChangeBorrowApproveConfiguration))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ChangeBorrowItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('change_borrow', 'change_return_at', 'id', 'thing', 'thing_circulation')
    change_borrow = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrow), graphql_name='changeBorrow')
    change_return_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='changeReturnAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    thing = sgqlc.types.Field(sgqlc.types.non_null('Thing'), graphql_name='thing')
    thing_circulation = sgqlc.types.Field(sgqlc.types.non_null('ThingCirculation'), graphql_name='thingCirculation')


class ChangeBorrowItemList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ChangeBorrowItem))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ChangeBorrowList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ChangeBorrow))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ChangeBorrowOperatorRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('created_at', 'id', 'operate_type', 'operator', 'opinion')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operate_type = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowOperatorType), graphql_name='operateType')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    opinion = sgqlc.types.Field(String, graphql_name='opinion')


class ChangeBorrowStateOverview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('finished_count', 'not_pass_count', 'pending_count', 'total_count', 'under_review_by_apply_for_count', 'under_review_by_borrowed_count')
    finished_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='finishedCount')
    not_pass_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='notPassCount')
    pending_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pendingCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    under_review_by_apply_for_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='underReviewByApplyForCount')
    under_review_by_borrowed_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='underReviewByBorrowedCount')


class City(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('counties', 'id', 'name', 'province_id')
    counties = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('County')), graphql_name='counties')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    province_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='provinceId')


class CodeRuleConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('configuration', 'rule')
    configuration = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='configuration')
    rule = sgqlc.types.Field(sgqlc.types.non_null(CodeRuleConfigurationRule), graphql_name='rule')


class Company(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('address', 'city', 'contact', 'county', 'email', 'id', 'is_mine', 'name', 'phone', 'province', 'type', 'uid', 'uscc')
    address = sgqlc.types.Field(String, graphql_name='address')
    city = sgqlc.types.Field(String, graphql_name='city')
    contact = sgqlc.types.Field(String, graphql_name='contact')
    county = sgqlc.types.Field(String, graphql_name='county')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_mine = sgqlc.types.Field(Boolean, graphql_name='isMine')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    type = sgqlc.types.Field(sgqlc.types.non_null('CompanyType'), graphql_name='type')
    uid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uid')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')


class CompanyBIDatasource(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app', 'created_at', 'datasource', 'id')
    app = sgqlc.types.Field(sgqlc.types.non_null(App), graphql_name='app')
    created_at = sgqlc.types.Field(Timestamp, graphql_name='createdAt')
    datasource = sgqlc.types.Field(sgqlc.types.non_null(BIDatasource), graphql_name='datasource')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class CompanyBIDatasourceList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CompanyBIDatasource)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CompanyList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Company)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CompanyThingCategoryUCCField(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'id', 'key', 'name')
    data = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='data')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CompanyThingCategoryUCCFieldList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompanyThingCategoryUCCField))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CompanyThingDepartmentScope(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'scope')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    scope = sgqlc.types.Field(sgqlc.types.non_null(ThingDepartmentScope), graphql_name='scope')


class CompanyThingGroupNode(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'thing_groups')
    company = sgqlc.types.Field(sgqlc.types.non_null(Company), graphql_name='company')
    thing_groups = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='thingGroups')


class CompanyType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Content(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('targets', 'template', 'url')
    targets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Field'))), graphql_name='targets')
    template = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='template')
    url = sgqlc.types.Field(String, graphql_name='url')


class Country(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('alpha2', 'alpha3', 'chinese', 'english', 'id')
    alpha2 = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='alpha2')
    alpha3 = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='alpha3')
    chinese = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='chinese')
    english = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='english')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')


class County(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('city_id', 'companies', 'id', 'name')
    city_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cityId')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Company)), graphql_name='companies')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreatedAccountInfo(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('account_id', 'password')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accountId')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')


class DayOfYear(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('day', 'month')
    day = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='day')
    month = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='month')


class DeleteThingResult(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('is_successful', 'limited_thing')
    is_successful = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSuccessful')
    limited_thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('LimitedThing')), graphql_name='limitedThing')


class Department(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'id', 'is_deleted', 'level', 'manager', 'name', 'organization_id', 'parent_id', 'path_name')
    code = sgqlc.types.Field(String, graphql_name='code')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_deleted = sgqlc.types.Field(Boolean, graphql_name='isDeleted')
    level = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='level')
    manager = sgqlc.types.Field('User', graphql_name='manager')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='organizationId')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentID')
    path_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pathName')


class DepartmentThingAdministrator(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('administrator', 'department', 'id')
    administrator = sgqlc.types.Field('User', graphql_name='administrator')
    department = sgqlc.types.Field(sgqlc.types.non_null(Department), graphql_name='department')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class DepartmentThingAdministratorList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DepartmentThingAdministrator))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Depository(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('factory', 'id', 'name')
    factory = sgqlc.types.Field(sgqlc.types.non_null('Factory'), graphql_name='factory')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class DepositoryList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Depository))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeptThingGroupList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DeptThingGroups')), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeptThingGroups(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('department', 'thing_groups')
    department = sgqlc.types.Field(sgqlc.types.non_null(Department), graphql_name='department')
    thing_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingGroup')), graphql_name='thingGroups')


class EamExcelValidationResult(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('abnormal_row_count', 'commented_data', 'duplicated_row_count', 'is_data_valid', 'is_header_valid', 'missing_fields', 'normal_row_count', 'redundant_fields', 'total_row_count')
    abnormal_row_count = sgqlc.types.Field(Int, graphql_name='abnormalRowCount')
    commented_data = sgqlc.types.Field('TempFile', graphql_name='commentedData')
    duplicated_row_count = sgqlc.types.Field(Int, graphql_name='duplicatedRowCount')
    is_data_valid = sgqlc.types.Field(Boolean, graphql_name='isDataValid')
    is_header_valid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isHeaderValid')
    missing_fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='missingFields')
    normal_row_count = sgqlc.types.Field(Int, graphql_name='normalRowCount')
    redundant_fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='redundantFields')
    total_row_count = sgqlc.types.Field(Int, graphql_name='totalRowCount')


class EamField(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('desc', 'form', 'group', 'id', 'is_active', 'is_lock', 'meta', 'name', 'operator', 'required_modify', 'role', 'type', 'updated_at')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    form = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('EamFormStructure')), graphql_name='form')
    group = sgqlc.types.Field(sgqlc.types.non_null(EamFieldGroupType), graphql_name='group')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    is_lock = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLock')
    meta = sgqlc.types.Field('EamMeta', graphql_name='meta')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    operator = sgqlc.types.Field('User', graphql_name='operator')
    required_modify = sgqlc.types.Field(Boolean, graphql_name='requiredModify')
    role = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='role')
    type = sgqlc.types.Field(sgqlc.types.non_null(EamFieldType), graphql_name='type')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class EamFieldList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EamField))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EamFieldSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('active_count', 'inactive_count', 'total_count')
    active_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='activeCount')
    inactive_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='inactiveCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EamFile(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('file_name', 'id', 'length', 'name', 'url')
    file_name = sgqlc.types.Field(String, graphql_name='fileName')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    length = sgqlc.types.Field(Int, graphql_name='length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class EamFormField(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('editable', 'field', 'option', 'required', 'width')
    editable = sgqlc.types.Field(Boolean, graphql_name='editable')
    field = sgqlc.types.Field(EamField, graphql_name='field')
    option = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('EamFormFieldOption')), graphql_name='option')
    required = sgqlc.types.Field(Boolean, graphql_name='required')
    width = sgqlc.types.Field(Int, graphql_name='width')


class EamFormFieldOption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('field', 'option')
    field = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EamField)), graphql_name='field')
    option = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='option')


class EamFormStructure(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_default', 'name', 'thing_category', 'zone')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_category = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingCategory'))), graphql_name='thingCategory')
    zone = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('EamZone')), graphql_name='zone')


class EamImportResult(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('failed_data', 'failed_row_count', 'is_all_successful', 'successful_row_count', 'total_row_count')
    failed_data = sgqlc.types.Field('TempFile', graphql_name='failedData')
    failed_row_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='failedRowCount')
    is_all_successful = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAllSuccessful')
    successful_row_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='successfulRowCount')
    total_row_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalRowCount')


class EamMetaAttachment(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('attachment_type', 'extension', 'hint', 'id', 'max_count', 'max_size', 'type')
    attachment_type = sgqlc.types.Field(EamAttachmentType, graphql_name='attachmentType')
    extension = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='extension')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    max_count = sgqlc.types.Field(Int, graphql_name='maxCount')
    max_size = sgqlc.types.Field(Int, graphql_name='maxSize')
    type = sgqlc.types.Field(sgqlc.types.non_null(EamFieldType), graphql_name='type')


class EamMetaDate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default_bool', 'format', 'hint', 'id', 'type')
    default_bool = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='defaultBool')
    format = sgqlc.types.Field(String, graphql_name='format')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(EamFieldType), graphql_name='type')


class EamMetaLabel(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('content', 'id', 'type')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(EamFieldType), graphql_name='type')


class EamMetaMultiRadio(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default_str_list', 'id', 'option', 'type')
    default_str_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='defaultStrList')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    option = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='option')
    type = sgqlc.types.Field(sgqlc.types.non_null(EamFieldType), graphql_name='type')


class EamMetaNumber(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default_num', 'hint', 'id', 'max', 'min', 'round', 'type', 'unit', 'zeroable')
    default_num = sgqlc.types.Field(Float, graphql_name='defaultNum')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    max = sgqlc.types.Field(Float, graphql_name='max')
    min = sgqlc.types.Field(Float, graphql_name='min')
    round = sgqlc.types.Field(Int, graphql_name='round')
    type = sgqlc.types.Field(sgqlc.types.non_null(EamFieldType), graphql_name='type')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    zeroable = sgqlc.types.Field(Boolean, graphql_name='zeroable')


class EamMetaOther(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'meta', 'type')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    meta = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('EamMetaOther')), graphql_name='meta')
    type = sgqlc.types.Field(sgqlc.types.non_null(EamFieldType), graphql_name='type')


class EamMetaRadio(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default_str', 'id', 'option', 'type')
    default_str = sgqlc.types.Field(String, graphql_name='defaultStr')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    option = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='option')
    type = sgqlc.types.Field(sgqlc.types.non_null(EamFieldType), graphql_name='type')


class EamMetaRange(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'max_range', 'min_range', 'type')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    max_range = sgqlc.types.Field(sgqlc.types.non_null('EamMetaRangeExtremum'), graphql_name='maxRange')
    min_range = sgqlc.types.Field(sgqlc.types.non_null('EamMetaRangeExtremum'), graphql_name='minRange')
    type = sgqlc.types.Field(sgqlc.types.non_null(EamFieldType), graphql_name='type')


class EamMetaRangeExtremum(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default', 'hint', 'id', 'max', 'min', 'round', 'unit', 'zeroable')
    default = sgqlc.types.Field(Float, graphql_name='default')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    max = sgqlc.types.Field(Float, graphql_name='max')
    min = sgqlc.types.Field(Float, graphql_name='min')
    round = sgqlc.types.Field(Int, graphql_name='round')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    zeroable = sgqlc.types.Field(Boolean, graphql_name='zeroable')


class EamMetaSelectBox(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default_str', 'default_str_list', 'hint', 'id', 'multi', 'option', 'type')
    default_str = sgqlc.types.Field(String, graphql_name='defaultStr')
    default_str_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='defaultStrList')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    multi = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='multi')
    option = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='option')
    type = sgqlc.types.Field(sgqlc.types.non_null(EamFieldType), graphql_name='type')


class EamMetaSet(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('meta', 'type')
    meta = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('EamMeta')), graphql_name='meta')
    type = sgqlc.types.Field(sgqlc.types.non_null(EamFieldType), graphql_name='type')


class EamMetaText(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default_str', 'hint', 'id', 'type')
    default_str = sgqlc.types.Field(String, graphql_name='defaultStr')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(EamFieldType), graphql_name='type')


class EamSparePartCategory(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'parent_id', 'path_info')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(Int, graphql_name='parentId')
    path_info = sgqlc.types.Field(sgqlc.types.non_null('EamSparePartCategoryPathInfo'), graphql_name='pathInfo')


class EamSparePartCategoryList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EamSparePartCategory))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EamSparePartCategoryPathInfo(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('path_name', 'top_category_name')
    path_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pathName')
    top_category_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='topCategoryName')


class EamSparePartFormStructure(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'zone')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    zone = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('EamZone')), graphql_name='zone')


class EamSparePartWarehouse(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class EamSparePartWarehouseList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EamSparePartWarehouse))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EamZone(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('field', 'group')
    field = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EamFormField)), graphql_name='field')
    group = sgqlc.types.Field(EamFieldGroupType, graphql_name='group')


class EvasionDate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('end_date', 'id', 'name', 'start_date')
    end_date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endDate')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    start_date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startDate')


class EvasionDateList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EvasionDate))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Factory(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class FactoryList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Factory))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FeaturePack(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('applicable_industries', 'apps', 'id', 'is_be_used', 'is_confirmed', 'name', 'remark')
    applicable_industries = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TenantIndustry'))), graphql_name='applicableIndustries')
    apps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(App))), graphql_name='apps')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    is_be_used = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isBeUsed')
    is_confirmed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isConfirmed')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class FeaturePackApp(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app_id', 'feature_pack_id', 'id')
    app_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='appId')
    feature_pack_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='featurePackId')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')


class FeaturePackApplicableIndustry(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('applicable_industry_id', 'feature_pack_id', 'id')
    applicable_industry_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='applicableIndustryId')
    feature_pack_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='featurePackId')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')


class FeaturePackList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FeaturePack))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FeaturePackPermission(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('feature_pack_id', 'id', 'permission_id')
    feature_pack_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='featurePackId')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    permission_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='permissionId')


class FeaturePackSubscription(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('expired_at', 'feature_pack', 'id', 'is_always_effective', 'is_expired', 'subscribed_at', 'subscriber')
    expired_at = sgqlc.types.Field(Timestamp, graphql_name='expiredAt')
    feature_pack = sgqlc.types.Field(sgqlc.types.non_null(FeaturePack), graphql_name='featurePack')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    is_always_effective = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAlwaysEffective')
    is_expired = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isExpired')
    subscribed_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='subscribedAt')
    subscriber = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='subscriber')


class Field(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'description', 'example', 'is_target', 'name')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    description = sgqlc.types.Field(String, graphql_name='description')
    example = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='example')
    is_target = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTarget')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class File(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'length', 'name', 'url')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    length = sgqlc.types.Field(Int, graphql_name='length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class GroupFile(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('file', 'is_complete_file', 'name')
    file = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EamFile))), graphql_name='file')
    is_complete_file = sgqlc.types.Field(Boolean, graphql_name='isCompleteFile')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Image(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'url')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class InboxMessage(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('content', 'created_at', 'id', 'is_read', 'kind', 'source_app', 'title', 'url')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    is_read = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRead')
    kind = sgqlc.types.Field(sgqlc.types.non_null(MessageKind), graphql_name='kind')
    source_app = sgqlc.types.Field(sgqlc.types.non_null(App), graphql_name='sourceApp')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    url = sgqlc.types.Field(String, graphql_name='url')


class InboxMessageList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'read_count', 'total_count', 'unread_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InboxMessage))), graphql_name='data')
    read_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='readCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    unread_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='unreadCount')


class InspectionMethod(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('field_data', 'id', 'name', 'thing_label')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_label = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingLabel'))), graphql_name='thingLabel')


class InspectionMethodList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InspectionMethod))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class InspectionOperatorRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('cost_time', 'created_at', 'id', 'operator', 'operator_record_type', 'remark', 'restart_operator', 'turn_to')
    cost_time = sgqlc.types.Field(Int, graphql_name='costTime')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    operator_record_type = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionOperatorType), graphql_name='operatorRecordType')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    restart_operator = sgqlc.types.Field('User', graphql_name='restartOperator')
    turn_to = sgqlc.types.Field('User', graphql_name='turnTo')


class InspectionProcessItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'image', 'inspection_method', 'is_finished', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EamFile))), graphql_name='image')
    inspection_method = sgqlc.types.Field(sgqlc.types.non_null(InspectionMethod), graphql_name='inspectionMethod')
    is_finished = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFinished')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class LimitedThing(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('reason', 'thing')
    reason = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DeleteThingLimitedReason))), graphql_name='reason')
    thing = sgqlc.types.Field(sgqlc.types.non_null('Thing'), graphql_name='thing')


class Log(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('account', 'action', 'app', 'code', 'details', 'feature', 'id', 'ip', 'location', 'occurred_at', 'payload', 'tenant_id')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    action = sgqlc.types.Field(sgqlc.types.non_null(LogAction), graphql_name='action')
    app = sgqlc.types.Field(sgqlc.types.non_null(App), graphql_name='app')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    details = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('OperationDetail')), graphql_name='details')
    feature = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='feature')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    ip = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ip')
    location = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='location')
    occurred_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='occurredAt')
    payload = sgqlc.types.Field(JSON, graphql_name='payload')
    tenant_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tenantId')


class LogList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Log))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class LoginConfig(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('assignable_modes', 'default_mode', 'id', 'modes')
    assignable_modes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LoginMode))), graphql_name='assignableModes')
    default_mode = sgqlc.types.Field(sgqlc.types.non_null(LoginMode), graphql_name='defaultMode')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    modes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LoginMode))), graphql_name='modes')


class LoginConfiguration(sgqlc.types.Interface):
    __schema__ = platform_schema
    __field_names__ = ('kind',)
    kind = sgqlc.types.Field(sgqlc.types.non_null(LoginConfigurationKind), graphql_name='kind')


class MaintenanceMethod(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('field_data', 'id', 'name', 'thing_label')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_label = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingLabel'))), graphql_name='thingLabel')


class MaintenanceMethodList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MaintenanceMethod))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MaintenanceProcessItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'image', 'is_finished', 'maintenance_method', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EamFile))), graphql_name='image')
    is_finished = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFinished')
    maintenance_method = sgqlc.types.Field(sgqlc.types.non_null(MaintenanceMethod), graphql_name='maintenanceMethod')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class MaintenanceSparePartItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'spare_part', 'spare_part_outbound')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null('SparePart'), graphql_name='sparePart')
    spare_part_outbound = sgqlc.types.Field(sgqlc.types.non_null('SparePartOutbound'), graphql_name='sparePartOutbound')


class Menu(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app', 'code', 'id', 'name', 'path_name', 'route')
    app = sgqlc.types.Field(App, graphql_name='app')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    path_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pathName')
    route = sgqlc.types.Field(String, graphql_name='route')


class MenuVisitHistory(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('access_at', 'menu')
    access_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='accessAt')
    menu = sgqlc.types.Field(sgqlc.types.non_null(Menu), graphql_name='menu')


class MenuVisitHistoryList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MenuVisitHistory))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MessageChannel(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('available_message_kind', 'description', 'id', 'kind', 'name', 'status')
    available_message_kind = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MessageKind))), graphql_name='availableMessageKind')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    kind = sgqlc.types.Field(MessageChannelKind, graphql_name='kind')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    status = sgqlc.types.Field(ChannelStatus, graphql_name='status')


class MessageTemplate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app', 'available_channels', 'contents', 'description', 'event', 'fields', 'id', 'name', 'render_styles', 'selected_channels', 'tenant_id')
    app = sgqlc.types.Field(sgqlc.types.non_null(App), graphql_name='app')
    available_channels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MessageChannel))), graphql_name='availableChannels')
    contents = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Content))), graphql_name='contents')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    event = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='event')
    fields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Field)), graphql_name='fields')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    render_styles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RenderStyle'))), graphql_name='renderStyles')
    selected_channels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MessageChannel))), graphql_name='selectedChannels')
    tenant_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tenantId')


class MessageTemplateList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MessageTemplate))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MetaChannel(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('available_message_kinds', 'description', 'id', 'name')
    available_message_kinds = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MessageKind))), graphql_name='availableMessageKinds')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class MetaTemplate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app', 'available_channels', 'contents', 'description', 'event', 'fields', 'has_updates', 'id', 'name', 'push_schedule', 'render_styles', 'status')
    app = sgqlc.types.Field(sgqlc.types.non_null(App), graphql_name='app')
    available_channels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MessageChannel))), graphql_name='availableChannels')
    contents = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Content))), graphql_name='contents')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    event = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='event')
    fields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Field)), graphql_name='fields')
    has_updates = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasUpdates')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    push_schedule = sgqlc.types.Field('PushSchedule', graphql_name='pushSchedule')
    render_styles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RenderStyle'))), graphql_name='renderStyles')
    status = sgqlc.types.Field(TemplateStatus, graphql_name='status')


class MetaTemplateList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MetaTemplate))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Mutation(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('_dummy', '_eam', 'accept_tenant_certification', 'accept_thing_inspection', 'accept_thing_maintenance', 'accept_thing_repair', 'activate_eam_form', 'active_message_channel', 'add_account_roles', 'add_feature_pack_to_tenant', 'add_meta_templates_to_tenant', 'add_thing_borrow_draft', 'add_thing_change_borrow_draft', 'add_thing_transfer_records', 'add_thing_transfer_records_by_code', 'admin_unbind_wecom_user', 'apply_for_tenant_certification', 'approve_change_borrow', 'approve_thing_calibrate', 'approve_thing_maintenance', 'approve_thing_repair', 'assign_app_permissions', 'assign_tenant_apps', 'bind_my_email', 'bind_my_phone_number', 'bind_wecom_user', 'cancel_spare_part_claim', 'change_my_password', 'change_my_password_by_email_verification', 'change_my_password_by_verify_code', 'company_login', 'configure_authentication_source_ldap3', 'configure_authentication_source_oauth2', 'configure_authentication_source_open_idconnect1', 'configure_authentication_source_saml2', 'confirm_borrow', 'confirm_borrow_by_thing', 'confirm_feature_pack', 'confirm_return', 'confirm_return_by_thing', 'confirm_spare_part_claim', 'copy_eam_form', 'copy_thing_bar_label', 'create_account', 'create_app_version', 'create_calibrate_organization', 'create_calibrate_schedule', 'create_change_borrow_approve_configuration', 'create_company_bidatasource', 'create_company_thing_category_uccfield', 'create_depository', 'create_eam_field', 'create_eam_file', 'create_eam_files', 'create_eam_spare_part_category', 'create_eam_spare_part_warehouse', 'create_enterprise_app', 'create_evasion_date', 'create_factory', 'create_feature_pack', 'create_file', 'create_files', 'create_image', 'create_images', 'create_inspection_method', 'create_maintenance_method', 'create_market_file', 'create_market_files', 'create_meta_template', 'create_oauth2_authentication_configuration', 'create_open_idconnect1_authentication_configuration', 'create_organization', 'create_outside_calibrate', 'create_role', 'create_spare_part', 'create_spare_part_claim', 'create_spare_part_outbound', 'create_spare_part_receipt', 'create_spare_part_transfer', 'create_spare_part_usage_record', 'create_spare_part_writeoff', 'create_staff', 'create_tenant', 'create_tenant_owner', 'create_thing', 'create_thing_administrator_department', 'create_thing_area', 'create_thing_attachment_type', 'create_thing_bar_label', 'create_thing_borrow', 'create_thing_borrow_approve_configuration', 'create_thing_calibrate', 'create_thing_calibrate_operator', 'create_thing_category', 'create_thing_category_uccfield', 'create_thing_change_borrow_by_draft', 'create_thing_complete_file_rule', 'create_thing_group', 'create_thing_inspection', 'create_thing_inspection_workflow_configuration', 'create_thing_inventory_redundant_record', 'create_thing_inventory_ticket', 'create_thing_label', 'create_thing_maintenance', 'create_thing_maintenance_workflow_configuration', 'create_thing_repair', 'create_thing_repair_workflow_configuration', 'create_thing_schedule', 'create_thing_ucc', 'deactivate_message_channel', 'delete_account', 'delete_app_version', 'delete_authentication_configuration', 'delete_calibrate_organization', 'delete_calibrate_schedule', 'delete_change_borrow_approve_configuration', 'delete_company_bidatasource', 'delete_company_thing_category_uccfield', 'delete_department_thing_groups', 'delete_depository', 'delete_eam_field', 'delete_eam_form', 'delete_eam_spare_part_category', 'delete_eam_spare_part_warehouse', 'delete_enterprise_apps', 'delete_evasion_date', 'delete_factory', 'delete_feature_pack', 'delete_inspection_method', 'delete_maintenance_method', 'delete_message_templates_of_tenant', 'delete_meta_template', 'delete_organization', 'delete_outside_calibrate', 'delete_role', 'delete_spare_part', 'delete_staff', 'delete_table_fields_config', 'delete_tenant', 'delete_thing', 'delete_thing_area', 'delete_thing_attachment_type', 'delete_thing_bar_label', 'delete_thing_borrow_approve_configuration', 'delete_thing_borrow_draft_thing', 'delete_thing_calibrate_operator', 'delete_thing_category', 'delete_thing_category_uccfield', 'delete_thing_change_borrow_draft_thing', 'delete_thing_complete_file_rule', 'delete_thing_group', 'delete_thing_inspection_workflow_configuration', 'delete_thing_inventory_redundant_record', 'delete_thing_label', 'delete_thing_maintenance_workflow_configuration', 'delete_thing_repair_workflow_configuration', 'delete_thing_schedule', 'delete_thing_task', 'delete_thing_ucc', 'delete_user_thing_groups', 'disable_tenant', 'duplicate_uccform_structure', 'enable_tenant', 'end_thing_inventory_ticket', 'finish_thing_inspection', 'finish_thing_maintenance', 'finish_thing_repair', 'generate_code', 'import_inspection_method', 'import_maintenance_method', 'import_spare_part', 'import_thing', 'import_thing_area', 'import_thing_category', 'import_thing_label', 'import_thing_schedule', 'import_thing_schedule_thing', 'import_thing_spare_part', 'issue_spare_part_claim', 'login', 'login_by_email', 'login_by_phone_number', 'logout', 'mark_certification_result_notified', 'move_things', 'offline_app_version', 'online_app_version', 'operate_spare_part_claim', 'operate_thing_borrow', 'overwrite_message_template', 'pass_thing_inventory_record', 'pause_thing_maintenance', 'pause_thing_repair', 'read_all_inbox_messages', 'read_inbox_messages', 'rehire_staff', 'reject_change_borrow', 'reject_tenant_certification', 'reject_thing_calibrate', 'reject_thing_maintenance', 'reject_thing_repair', 'remove_account_roles', 'remove_calibrate_thing_category', 'remove_feature_pack_subscription', 'remove_thing_administrator_department', 'remove_thing_function_department', 'replace_thing_borrow', 'reset_account_password', 'reset_app_client_secret', 'reset_authentication_source', 'reset_tenant_owner_password', 'resign_staff', 'restart_thing_inspection', 'restart_thing_maintenance', 'restart_thing_repair', 'save_thing_calibrate', 'save_thing_inspection', 'save_thing_maintenance', 'save_thing_repair', 'send_identity_verify_code_to_email', 'send_identity_verify_code_to_my_phone_number', 'send_identity_verify_code_to_phone_number', 'send_identity_verify_code_to_un_verified_phone_number', 'set_admin_users', 'set_authorization_rules_data_range_of_role', 'set_authorization_rules_to_role', 'set_calibrate_thing_category', 'set_channel_of_message_templates', 'set_channels_of_message_template', 'set_code_rule_configuration', 'set_company_thing_department_scope', 'set_department_thing_group', 'set_departments_thing_group', 'set_eam_field_to_eam_form', 'set_eam_form_structure', 'set_eam_form_thing_category', 'set_eam_spare_part_form_structure', 'set_eam_spare_part_warehouse_manager', 'set_login_config_to_my_tenant', 'set_login_modes_to_tenant', 'set_organization_staffs', 'set_outside_calibrate_thing_calibrate', 'set_permissions_to_feature_pack', 'set_permissions_to_tenant', 'set_role_accounts', 'set_role_thing_category', 'set_single_department_thing_groups', 'set_single_user_thing_groups', 'set_spare_part_stock_configuration', 'set_spare_part_thing', 'set_spare_part_workflow_configuration', 'set_stared_pages', 'set_sub_thing', 'set_table_column_setting', 'set_table_fields_config', 'set_table_fixed_fields_config', 'set_thing_borrow_range_configuration', 'set_thing_borrow_workflow_configuration', 'set_thing_calibrate', 'set_thing_calibrate_range_configuration', 'set_thing_calibrate_workflow_configuration', 'set_thing_function_department', 'set_thing_inventory_record', 'set_thing_inventory_record_by_thing', 'set_thing_schedule_thing', 'set_thing_spare_part', 'set_uccform_structure', 'set_uccstack_data', 'set_users_thing_group', 'set_workbench', 'sign_up_tenant', 'star_app', 'star_pages', 'start_thing_inventory_ticket', 'submit_change_borrow', 'submit_thing_borrow', 'submit_thing_calibrate', 'track_thing_inventory_ticket', 'transfer_organization', 'transfer_tenant_owner', 'turn_to_thing_calibrate', 'turn_to_thing_inspection', 'turn_to_thing_maintenance', 'turn_to_thing_repair', 'un_assign_app_permissions', 'un_assign_tenant_apps', 'un_star_app', 'un_star_pages', 'unbind_email_of_users', 'unbind_my_email', 'unbind_my_phone_number', 'unbind_phone_number_of_users', 'unbind_wecom_user', 'unset_admin_users', 'update_account', 'update_app_version', 'update_authorization_rule', 'update_calibrate_organization', 'update_calibrate_schedule', 'update_change_borrow_approve_configuration', 'update_company_thing_category_uccfield', 'update_department_thing_administrator', 'update_department_thing_group', 'update_depository', 'update_eam_field', 'update_eam_spare_part_category', 'update_eam_spare_part_warehouse', 'update_enterprise_app', 'update_evasion_date', 'update_factory', 'update_feature_pack', 'update_inspection_method', 'update_maintenance_method', 'update_me', 'update_meta_channel', 'update_meta_template', 'update_oauth2_authentication_configuration', 'update_open_idconnect1_authentication_configuration', 'update_organization', 'update_outside_calibrate', 'update_role', 'update_spare_part', 'update_spare_part_claim', 'update_staff', 'update_status_of_template', 'update_tenant', 'update_thing', 'update_thing_area', 'update_thing_attachment_type', 'update_thing_bar_label', 'update_thing_borrow', 'update_thing_borrow_approve_configuration', 'update_thing_borrow_draft_thing', 'update_thing_by_code', 'update_thing_calibrate_operator', 'update_thing_category', 'update_thing_category_uccfield', 'update_thing_change_borrow_by_draft', 'update_thing_change_borrow_draft_thing', 'update_thing_complete_file_rule', 'update_thing_function_departments', 'update_thing_group', 'update_thing_inspection_workflow_configuration', 'update_thing_inventory_redundant_record', 'update_thing_label', 'update_thing_maintenance_workflow_configuration', 'update_thing_repair_workflow_configuration', 'update_thing_schedule', 'update_thing_task', 'update_thing_ucc', 'update_things', 'update_user_thing_group', 'update_workflow_base_configuration', 'use_spare_part_claim', 'visit_app', 'visit_menu', 'wecom_app_login', 'wecom_login', 'writeoff_spare_part_receipt')
    _dummy = sgqlc.types.Field(Boolean, graphql_name='_dummy')
    _eam = sgqlc.types.Field(Boolean, graphql_name='_eam')
    accept_tenant_certification = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='acceptTenantCertification', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    accept_thing_inspection = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='acceptThingInspection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    accept_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='acceptThingMaintenance', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    accept_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='acceptThingRepair', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    activate_eam_form = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='activateEamForm', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    active_message_channel = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='activeMessageChannel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    add_account_roles = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addAccountRoles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddAccountRolesInput), graphql_name='input', default=None)),
))
    )
    add_feature_pack_to_tenant = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addFeaturePackToTenant', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddFeaturePackToTenant), graphql_name='input', default=None)),
))
    )
    add_meta_templates_to_tenant = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addMetaTemplatesToTenant', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ids', default=None)),
        ('tenant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tenantId', default=None)),
))
    )
    add_thing_borrow_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addThingBorrowDraft', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddThingBorrowDraftInput), graphql_name='input', default=None)),
))
    )
    add_thing_change_borrow_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addThingChangeBorrowDraft', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddThingChangeBorrowDraftInput), graphql_name='input', default=None)),
))
    )
    add_thing_transfer_records = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addThingTransferRecords', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddThingTransferRecordInput), graphql_name='input', default=None)),
))
    )
    add_thing_transfer_records_by_code = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addThingTransferRecordsByCode', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddThingTransferRecordByCodeInput), graphql_name='input', default=None)),
))
    )
    admin_unbind_wecom_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='adminUnbindWecomUser', args=sgqlc.types.ArgDict((
        ('account_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='accountId', default=None)),
))
    )
    apply_for_tenant_certification = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='applyForTenantCertification', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ApplyForTenantCertificationInput), graphql_name='input', default=None)),
))
    )
    approve_change_borrow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='approveChangeBorrow', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ApproveChangeBorrowInput), graphql_name='input', default=None)),
))
    )
    approve_thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='approveThingCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ApproveThingCalibrateInput), graphql_name='input', default=None)),
))
    )
    approve_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='approveThingMaintenance', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    approve_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='approveThingRepair', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    assign_app_permissions = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='assignAppPermissions', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AssignAppPermissionsInput), graphql_name='input', default=None)),
))
    )
    assign_tenant_apps = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='assignTenantApps', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AssignTenantAppsInput), graphql_name='input', default=None)),
))
    )
    bind_my_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='bindMyEmail', args=sgqlc.types.ArgDict((
        ('verify_code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='verifyCode', default=None)),
))
    )
    bind_my_phone_number = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='bindMyPhoneNumber', args=sgqlc.types.ArgDict((
        ('verify_code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='verifyCode', default=None)),
))
    )
    bind_wecom_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='bindWecomUser', args=sgqlc.types.ArgDict((
        ('auth_code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='authCode', default=None)),
))
    )
    cancel_spare_part_claim = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='cancelSparePartClaim', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    change_my_password = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='changeMyPassword', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ChangeMyPasswordInput), graphql_name='input', default=None)),
))
    )
    change_my_password_by_email_verification = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='changeMyPasswordByEmailVerification', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ChangeMyPasswordByEmailVerificationInput), graphql_name='input', default=None)),
))
    )
    change_my_password_by_verify_code = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='changeMyPasswordByVerifyCode', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ChangeMyPasswordByVerifyCodeInput), graphql_name='input', default=None)),
))
    )
    company_login = sgqlc.types.Field(sgqlc.types.non_null(AuthInfo), graphql_name='companyLogin', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CompanyLoginInput), graphql_name='input', default=None)),
))
    )
    configure_authentication_source_ldap3 = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='configureAuthenticationSourceLDAP3', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ConfigureAuthenticationSourceLDAP3Input), graphql_name='input', default=None)),
))
    )
    configure_authentication_source_oauth2 = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='configureAuthenticationSourceOAuth2', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ConfigureAuthenticationSourceOAuth2Input), graphql_name='input', default=None)),
))
    )
    configure_authentication_source_open_idconnect1 = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='configureAuthenticationSourceOpenIDConnect1', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ConfigureAuthenticationSourceOpenIDConnect1Input), graphql_name='input', default=None)),
))
    )
    configure_authentication_source_saml2 = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='configureAuthenticationSourceSAML2', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ConfigureAuthenticationSourceSAML2Input), graphql_name='input', default=None)),
))
    )
    confirm_borrow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='confirmBorrow', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ConfirmBorrowInput), graphql_name='input', default=None)),
))
    )
    confirm_borrow_by_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='confirmBorrowByThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ConfirmBorrowByThingInput), graphql_name='input', default=None)),
))
    )
    confirm_feature_pack = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='confirmFeaturePack', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    confirm_return = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='confirmReturn', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ConfirmReturnInput), graphql_name='input', default=None)),
))
    )
    confirm_return_by_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='confirmReturnByThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ConfirmReturnByThingInput), graphql_name='input', default=None)),
))
    )
    confirm_spare_part_claim = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='confirmSparePartClaim', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ConfirmSparePartClaimInput), graphql_name='input', default=None)),
))
    )
    copy_eam_form = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='copyEamForm', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    copy_thing_bar_label = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='copyThingBarLabel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    create_account = sgqlc.types.Field(sgqlc.types.non_null(CreatedAccountInfo), graphql_name='createAccount', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateAccountInput), graphql_name='input', default=None)),
))
    )
    create_app_version = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createAppVersion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateAppVersionInput), graphql_name='input', default=None)),
))
    )
    create_calibrate_organization = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createCalibrateOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCalibrateOrganizationInput), graphql_name='input', default=None)),
))
    )
    create_calibrate_schedule = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createCalibrateSchedule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCalibrateScheduleInput), graphql_name='input', default=None)),
))
    )
    create_change_borrow_approve_configuration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createChangeBorrowApproveConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateChangeBorrowApproveConfigurationInput, graphql_name='input', default=None)),
))
    )
    create_company_bidatasource = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createCompanyBIDatasource', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCompanyBIDatasourceInput), graphql_name='input', default=None)),
))
    )
    create_company_thing_category_uccfield = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createCompanyThingCategoryUCCField', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCompanyThingCategoryUCCFieldInput), graphql_name='input', default=None)),
))
    )
    create_depository = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createDepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateDepositoryInput), graphql_name='input', default=None)),
))
    )
    create_eam_field = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createEamField', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(EamFieldInput), graphql_name='input', default=None)),
))
    )
    create_eam_file = sgqlc.types.Field(sgqlc.types.non_null(EamFile), graphql_name='createEamFile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEamFileInput), graphql_name='input', default=None)),
))
    )
    create_eam_files = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EamFile)), graphql_name='createEamFiles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CreateEamFileInput))), graphql_name='input', default=None)),
))
    )
    create_eam_spare_part_category = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createEamSparePartCategory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEamSparePartCategoryInput), graphql_name='input', default=None)),
))
    )
    create_eam_spare_part_warehouse = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createEamSparePartWarehouse', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEamSparePartWarehouseInput), graphql_name='input', default=None)),
))
    )
    create_enterprise_app = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createEnterpriseApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEnterpriseAppInput), graphql_name='input', default=None)),
))
    )
    create_evasion_date = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createEvasionDate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEvasionDateInput), graphql_name='input', default=None)),
))
    )
    create_factory = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createFactory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFactoryInput), graphql_name='input', default=None)),
))
    )
    create_feature_pack = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createFeaturePack', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFeaturePackInput), graphql_name='input', default=None)),
))
    )
    create_file = sgqlc.types.Field(File, graphql_name='createFile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFileInput), graphql_name='input', default=None)),
))
    )
    create_files = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='createFiles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CreateFileInput)), graphql_name='input', default=None)),
))
    )
    create_image = sgqlc.types.Field(Image, graphql_name='createImage', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateImageInput), graphql_name='input', default=None)),
))
    )
    create_images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Image)), graphql_name='createImages', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CreateImageInput)), graphql_name='input', default=None)),
))
    )
    create_inspection_method = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createInspectionMethod', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateInspectionMethodInput), graphql_name='input', default=None)),
))
    )
    create_maintenance_method = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createMaintenanceMethod', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMaintenanceMethodInput), graphql_name='input', default=None)),
))
    )
    create_market_file = sgqlc.types.Field(sgqlc.types.non_null(File), graphql_name='createMarketFile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMarketFileInput), graphql_name='input', default=None)),
))
    )
    create_market_files = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='createMarketFiles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CreateMarketFileInput)), graphql_name='input', default=None)),
))
    )
    create_meta_template = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createMetaTemplate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMetaTemplateInput), graphql_name='input', default=None)),
))
    )
    create_oauth2_authentication_configuration = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createOAuth2AuthenticationConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateOAuth2AuthenticationConfigurationInput), graphql_name='input', default=None)),
))
    )
    create_open_idconnect1_authentication_configuration = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createOpenIDConnect1AuthenticationConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateOpenIDConnect1AuthenticationConfigurationInput), graphql_name='input', default=None)),
))
    )
    create_organization = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateOrganizationInput), graphql_name='input', default=None)),
))
    )
    create_outside_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createOutsideCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateOutsideCalibrateInput), graphql_name='input', default=None)),
))
    )
    create_role = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateRoleInput), graphql_name='input', default=None)),
))
    )
    create_spare_part = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createSparePart', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSparePartInput), graphql_name='input', default=None)),
))
    )
    create_spare_part_claim = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='createSparePartClaim', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSparePartClaimInput), graphql_name='input', default=None)),
))
    )
    create_spare_part_outbound = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createSparePartOutbound', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSparePartOutboundInput), graphql_name='input', default=None)),
))
    )
    create_spare_part_receipt = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createSparePartReceipt', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSparePartReceiptInput), graphql_name='input', default=None)),
))
    )
    create_spare_part_transfer = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createSparePartTransfer', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSparePartTransferInput), graphql_name='input', default=None)),
))
    )
    create_spare_part_usage_record = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createSparePartUsageRecord', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSparePartUsageRecordInput), graphql_name='input', default=None)),
))
    )
    create_spare_part_writeoff = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createSparePartWriteoff', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSparePartWriteoffInput), graphql_name='input', default=None)),
))
    )
    create_staff = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createStaff', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateStaffInput), graphql_name='input', default=None)),
))
    )
    create_tenant = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createTenant', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateTenantInput), graphql_name='input', default=None)),
))
    )
    create_tenant_owner = sgqlc.types.Field(sgqlc.types.non_null(CreatedAccountInfo), graphql_name='createTenantOwner', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateTenantOwnerInput), graphql_name='input', default=None)),
))
    )
    create_thing = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingInput), graphql_name='input', default=None)),
))
    )
    create_thing_administrator_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createThingAdministratorDepartment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingAdministratorDepartmentInput), graphql_name='input', default=None)),
))
    )
    create_thing_area = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingArea', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingAreaInput), graphql_name='input', default=None)),
))
    )
    create_thing_attachment_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingAttachmentType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingAttachmentTypeInput), graphql_name='input', default=None)),
))
    )
    create_thing_bar_label = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingBarLabel', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingBarLabelInput), graphql_name='input', default=None)),
))
    )
    create_thing_borrow = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='createThingBorrow', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetThingBorrowInput), graphql_name='input', default=None)),
))
    )
    create_thing_borrow_approve_configuration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingBorrowApproveConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateThingBorrowApproveConfigurationInput, graphql_name='input', default=None)),
))
    )
    create_thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='createThingCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingCalibrateInput), graphql_name='input', default=None)),
))
    )
    create_thing_calibrate_operator = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createThingCalibrateOperator', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingCalibrateOperatorInput), graphql_name='input', default=None)),
))
    )
    create_thing_category = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingCategory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingCategoryInput), graphql_name='input', default=None)),
))
    )
    create_thing_category_uccfield = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingCategoryUCCField', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingCategoryUCCFieldInput), graphql_name='input', default=None)),
))
    )
    create_thing_change_borrow_by_draft = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='createThingChangeBorrowByDraft', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('reason', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='reason', default=None)),
))
    )
    create_thing_complete_file_rule = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingCompleteFileRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingCompleteFileRuleInput), graphql_name='input', default=None)),
))
    )
    create_thing_group = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingGroupInput), graphql_name='input', default=None)),
))
    )
    create_thing_inspection = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingInspection', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingInspectionInput), graphql_name='input', default=None)),
))
    )
    create_thing_inspection_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingInspectionWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateThingInspectionWorkflowConfigurationInput, graphql_name='input', default=None)),
))
    )
    create_thing_inventory_redundant_record = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingInventoryRedundantRecord', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingInventoryRedundantRecordInput), graphql_name='input', default=None)),
))
    )
    create_thing_inventory_ticket = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingInventoryTicket', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingInventoryTicketInput), graphql_name='input', default=None)),
))
    )
    create_thing_label = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingLabel', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingLabelInput), graphql_name='input', default=None)),
))
    )
    create_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingMaintenance', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingMaintenanceInput), graphql_name='input', default=None)),
))
    )
    create_thing_maintenance_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingMaintenanceWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateThingMaintenanceWorkflowConfigurationInput, graphql_name='input', default=None)),
))
    )
    create_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingRepair', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingRepairInput), graphql_name='input', default=None)),
))
    )
    create_thing_repair_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingRepairWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateThingRepairWorkflowConfigurationInput, graphql_name='input', default=None)),
))
    )
    create_thing_schedule = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='createThingSchedule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingScheduleInput), graphql_name='input', default=None)),
))
    )
    create_thing_ucc = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingUCC', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingUCCInput), graphql_name='input', default=None)),
))
    )
    deactivate_message_channel = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deactivateMessageChannel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    delete_account = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteAccount', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    delete_app_version = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteAppVersion', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    delete_authentication_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteAuthenticationConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    delete_calibrate_organization = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCalibrateOrganization', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_calibrate_schedule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCalibrateSchedule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_change_borrow_approve_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteChangeBorrowApproveConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_company_bidatasource = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCompanyBIDatasource', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    delete_company_thing_category_uccfield = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCompanyThingCategoryUCCField', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_department_thing_groups = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteDepartmentThingGroups', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteDepartmentThingGroupInput), graphql_name='input', default=None)),
))
    )
    delete_depository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteDepository', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_eam_field = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteEamField', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_eam_form = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteEamForm', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_eam_spare_part_category = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteEamSparePartCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_eam_spare_part_warehouse = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteEamSparePartWarehouse', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_enterprise_apps = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteEnterpriseApps', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    delete_evasion_date = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteEvasionDate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_factory = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteFactory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_feature_pack = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteFeaturePack', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    delete_inspection_method = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteInspectionMethod', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_maintenance_method = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteMaintenanceMethod', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_message_templates_of_tenant = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteMessageTemplatesOfTenant', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ids', default=None)),
        ('tenant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tenantId', default=None)),
))
    )
    delete_meta_template = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteMetaTemplate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    delete_organization = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteOrganization', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    delete_outside_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteOutsideCalibrate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_role = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteRole', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    delete_spare_part = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteSparePart', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_staff = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteStaff', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    delete_table_fields_config = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteTableFieldsConfig', args=sgqlc.types.ArgDict((
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
))
    )
    delete_tenant = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteTenant', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    delete_thing = sgqlc.types.Field(sgqlc.types.non_null(DeleteThingResult), graphql_name='deleteThing', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    delete_thing_area = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingArea', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_attachment_type = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingAttachmentType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_bar_label = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingBarLabel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_borrow_approve_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingBorrowApproveConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_borrow_draft_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingBorrowDraftThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteThingBorrowDraftThingInput), graphql_name='input', default=None)),
))
    )
    delete_thing_calibrate_operator = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingCalibrateOperator', args=sgqlc.types.ArgDict((
        ('user', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput))), graphql_name='user', default=None)),
))
    )
    delete_thing_category = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_category_uccfield = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingCategoryUCCField', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_change_borrow_draft_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingChangeBorrowDraftThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteThingChangeBorrowDraftThingInput), graphql_name='input', default=None)),
))
    )
    delete_thing_complete_file_rule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingCompleteFileRule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingGroup', args=sgqlc.types.ArgDict((
        ('thing_group', sgqlc.types.Arg(sgqlc.types.non_null(IDInput), graphql_name='thingGroup', default=None)),
))
    )
    delete_thing_inspection_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingInspectionWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_inventory_redundant_record = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingInventoryRedundantRecord', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    delete_thing_label = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingLabel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_maintenance_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingMaintenanceWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_repair_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingRepairWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_schedule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingSchedule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_task = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingTask', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    delete_thing_ucc = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingUCC', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_user_thing_groups = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteUserThingGroups', args=sgqlc.types.ArgDict((
        ('thing_groups', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='thingGroups', default=None)),
))
    )
    disable_tenant = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='disableTenant', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    duplicate_uccform_structure = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='duplicateUCCFormStructure', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DuplicateUCCFormStructureInput), graphql_name='input', default=None)),
))
    )
    enable_tenant = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enableTenant', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    end_thing_inventory_ticket = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='endThingInventoryTicket', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    finish_thing_inspection = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='finishThingInspection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    finish_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='finishThingMaintenance', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    finish_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='finishThingRepair', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    generate_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='generateCode', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(GenerateCodeInput), graphql_name='input', default=None)),
))
    )
    import_inspection_method = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importInspectionMethod', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    import_maintenance_method = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importMaintenanceMethod', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    import_spare_part = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importSparePart', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    import_thing = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importThing', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    import_thing_area = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importThingArea', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    import_thing_category = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importThingCategory', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    import_thing_label = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importThingLabel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    import_thing_schedule = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importThingSchedule', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    import_thing_schedule_thing = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importThingScheduleThing', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    import_thing_spare_part = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importThingSparePart', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    issue_spare_part_claim = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='issueSparePartClaim', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IssueSparePartClaimInput), graphql_name='input', default=None)),
))
    )
    login = sgqlc.types.Field(sgqlc.types.non_null(AuthInfo), graphql_name='login', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(LoginInput), graphql_name='input', default=None)),
))
    )
    login_by_email = sgqlc.types.Field(sgqlc.types.non_null(AuthInfo), graphql_name='loginByEmail', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(LoginByEmailInput), graphql_name='input', default=None)),
))
    )
    login_by_phone_number = sgqlc.types.Field(sgqlc.types.non_null(AuthInfo), graphql_name='loginByPhoneNumber', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(LoginByPhoneNumberInput), graphql_name='input', default=None)),
))
    )
    logout = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='logout')
    mark_certification_result_notified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='markCertificationResultNotified', args=sgqlc.types.ArgDict((
        ('tenant_id', sgqlc.types.Arg(String, graphql_name='tenantId', default=None)),
))
    )
    move_things = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='moveThings', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MoveThingInput), graphql_name='input', default=None)),
))
    )
    offline_app_version = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='offlineAppVersion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    online_app_version = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='onlineAppVersion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    operate_spare_part_claim = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='operateSparePartClaim', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(OperateSparePartClaimInput), graphql_name='input', default=None)),
))
    )
    operate_thing_borrow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='operateThingBorrow', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(OperateThingBorrowInput), graphql_name='input', default=None)),
))
    )
    overwrite_message_template = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='overwriteMessageTemplate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    pass_thing_inventory_record = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='passThingInventoryRecord', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(PassThingInventoryRecordInput), graphql_name='input', default=None)),
))
    )
    pause_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='pauseThingMaintenance', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(PauseThingMaintenanceInput), graphql_name='input', default=None)),
))
    )
    pause_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='pauseThingRepair', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(PauseThingRepairInput), graphql_name='input', default=None)),
))
    )
    read_all_inbox_messages = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='readAllInboxMessages', args=sgqlc.types.ArgDict((
        ('source_app_keys', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sourceAppKeys', default=None)),
))
    )
    read_inbox_messages = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='readInboxMessages', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    rehire_staff = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='rehireStaff', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    reject_change_borrow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='rejectChangeBorrow', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RejectChangeBorrowInput), graphql_name='input', default=None)),
))
    )
    reject_tenant_certification = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='rejectTenantCertification', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RejectTenantCertificationInput), graphql_name='input', default=None)),
))
    )
    reject_thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='rejectThingCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RejectThingCalibrateInput), graphql_name='input', default=None)),
))
    )
    reject_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='rejectThingMaintenance', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RejectThingMaintenanceInput), graphql_name='input', default=None)),
))
    )
    reject_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='rejectThingRepair', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RejectThingRepairInput), graphql_name='input', default=None)),
))
    )
    remove_account_roles = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='removeAccountRoles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveAccountRolesInput), graphql_name='input', default=None)),
))
    )
    remove_calibrate_thing_category = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='removeCalibrateThingCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    remove_feature_pack_subscription = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='removeFeaturePackSubscription', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    remove_thing_administrator_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='removeThingAdministratorDepartment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    remove_thing_function_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='removeThingFunctionDepartment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    replace_thing_borrow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='replaceThingBorrow', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ReplaceThingBorrowInput), graphql_name='input', default=None)),
))
    )
    reset_account_password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='resetAccountPassword', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    reset_app_client_secret = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='resetAppClientSecret', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    reset_authentication_source = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='resetAuthenticationSource', args=sgqlc.types.ArgDict((
        ('company_uid', sgqlc.types.Arg(String, graphql_name='companyUID', default=None)),
))
    )
    reset_tenant_owner_password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='resetTenantOwnerPassword', args=sgqlc.types.ArgDict((
        ('tenant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tenantId', default=None)),
        ('user_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='userId', default=None)),
))
    )
    resign_staff = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='resignStaff', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    restart_thing_inspection = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restartThingInspection', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RestartThingInspectionInput), graphql_name='input', default=None)),
))
    )
    restart_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restartThingMaintenance', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RestartThingMaintenanceInput), graphql_name='input', default=None)),
))
    )
    restart_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restartThingRepair', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RestartThingRepairInput), graphql_name='input', default=None)),
))
    )
    save_thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='saveThingCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SaveThingCalibrateInput), graphql_name='input', default=None)),
))
    )
    save_thing_inspection = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='saveThingInspection', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SaveThingInspectionInput), graphql_name='input', default=None)),
))
    )
    save_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='saveThingMaintenance', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SaveThingMaintenanceInput), graphql_name='input', default=None)),
))
    )
    save_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='saveThingRepair', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SaveThingRepairInput), graphql_name='input', default=None)),
))
    )
    send_identity_verify_code_to_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='sendIdentityVerifyCodeToEmail', args=sgqlc.types.ArgDict((
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
))
    )
    send_identity_verify_code_to_my_phone_number = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='sendIdentityVerifyCodeToMyPhoneNumber')
    send_identity_verify_code_to_phone_number = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='sendIdentityVerifyCodeToPhoneNumber', args=sgqlc.types.ArgDict((
        ('phone_number', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='phoneNumber', default=None)),
))
    )
    send_identity_verify_code_to_un_verified_phone_number = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='sendIdentityVerifyCodeToUnVerifiedPhoneNumber', args=sgqlc.types.ArgDict((
        ('phone_number', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='phoneNumber', default=None)),
))
    )
    set_admin_users = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setAdminUsers', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    set_authorization_rules_data_range_of_role = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setAuthorizationRulesDataRangeOfRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetAuthorizationRulesToRoleInput), graphql_name='input', default=None)),
))
    )
    set_authorization_rules_to_role = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setAuthorizationRulesToRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetAuthorizationRulesToRoleInput), graphql_name='input', default=None)),
))
    )
    set_calibrate_thing_category = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setCalibrateThingCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    set_channel_of_message_templates = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setChannelOfMessageTemplates', args=sgqlc.types.ArgDict((
        ('channel_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='channelId', default=None)),
        ('message_template_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='messageTemplateIds', default=None)),
        ('tenant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tenantId', default=None)),
))
    )
    set_channels_of_message_template = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setChannelsOfMessageTemplate', args=sgqlc.types.ArgDict((
        ('channel_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='channelIds', default=None)),
        ('message_template_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='messageTemplateId', default=None)),
        ('tenant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tenantId', default=None)),
))
    )
    set_code_rule_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setCodeRuleConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetCodeRuleConfigurationInput), graphql_name='input', default=None)),
))
    )
    set_company_thing_department_scope = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setCompanyThingDepartmentScope', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetCompanyThingDepartmentScope), graphql_name='input', default=None)),
))
    )
    set_department_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setDepartmentThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetDepartmentThingGroup), graphql_name='input', default=None)),
))
    )
    set_departments_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setDepartmentsThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetDepartmentThingGroupInput), graphql_name='input', default=None)),
))
    )
    set_eam_field_to_eam_form = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setEamFieldToEamForm', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetEamFieldToEamFormInput), graphql_name='input', default=None)),
))
    )
    set_eam_form_structure = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='setEamFormStructure', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetEamFormStructureInput), graphql_name='input', default=None)),
))
    )
    set_eam_form_thing_category = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setEamFormThingCategory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetFormThingCategoryInput), graphql_name='input', default=None)),
))
    )
    set_eam_spare_part_form_structure = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='setEamSparePartFormStructure', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetEamSparePartFormStructureInput), graphql_name='input', default=None)),
))
    )
    set_eam_spare_part_warehouse_manager = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setEamSparePartWarehouseManager', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetEamSparePartWarehouseManager), graphql_name='input', default=None)),
))
    )
    set_login_config_to_my_tenant = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setLoginConfigToMyTenant', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetLoginConfigToMyTenantInput), graphql_name='input', default=None)),
))
    )
    set_login_modes_to_tenant = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setLoginModesToTenant', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetLoginModesToTenantInput), graphql_name='input', default=None)),
))
    )
    set_organization_staffs = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setOrganizationStaffs', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetOrganizationUsersInput), graphql_name='input', default=None)),
))
    )
    set_outside_calibrate_thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setOutsideCalibrateThingCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetOutsideCalibrateThingCalibrateInput), graphql_name='input', default=None)),
))
    )
    set_permissions_to_feature_pack = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setPermissionsToFeaturePack', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetPermissionToFeaturePackInput), graphql_name='input', default=None)),
))
    )
    set_permissions_to_tenant = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setPermissionsToTenant', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetPermissionToTenantInput), graphql_name='input', default=None)),
))
    )
    set_role_accounts = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setRoleAccounts', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetRoleAccountInput), graphql_name='input', default=None)),
))
    )
    set_role_thing_category = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setRoleThingCategory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetRoleThingCategory), graphql_name='input', default=None)),
))
    )
    set_single_department_thing_groups = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setSingleDepartmentThingGroups', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(SetSingleDepartmentThingGroups, graphql_name='input', default=None)),
))
    )
    set_single_user_thing_groups = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setSingleUserThingGroups', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetSingleUserThingGroupsInput), graphql_name='input', default=None)),
))
    )
    set_spare_part_stock_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setSparePartStockConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetSparePartStockConfigurationInput), graphql_name='input', default=None)),
))
    )
    set_spare_part_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setSparePartThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetSparePartThingInput), graphql_name='input', default=None)),
))
    )
    set_spare_part_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setSparePartWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetSparePartWorkflowConfigurationInput), graphql_name='input', default=None)),
))
    )
    set_stared_pages = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setStaredPages', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    set_sub_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setSubThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetSubThingInput), graphql_name='input', default=None)),
))
    )
    set_table_column_setting = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setTableColumnSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetTableColumnSettingInput), graphql_name='input', default=None)),
))
    )
    set_table_fields_config = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setTableFieldsConfig', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetTableFieldsConfigInput), graphql_name='input', default=None)),
))
    )
    set_table_fixed_fields_config = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setTableFixedFieldsConfig', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetTableFixedFieldsConfigInput), graphql_name='input', default=None)),
))
    )
    set_thing_borrow_range_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThingBorrowRangeConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetThingBorrowRangeConfigurationInput), graphql_name='input', default=None)),
))
    )
    set_thing_borrow_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThingBorrowWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetThingBorrowWorkflowConfigurationInput), graphql_name='input', default=None)),
))
    )
    set_thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThingCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetThingCalibrateInput), graphql_name='input', default=None)),
))
    )
    set_thing_calibrate_range_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThingCalibrateRangeConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetThingCalibrateRangeConfigurationInput), graphql_name='input', default=None)),
))
    )
    set_thing_calibrate_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThingCalibrateWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetThingCalibrateWorkflowConfigurationInput), graphql_name='input', default=None)),
))
    )
    set_thing_function_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThingFunctionDepartment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetThingDepartmentInput), graphql_name='input', default=None)),
))
    )
    set_thing_inventory_record = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThingInventoryRecord', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(SetThingInventoryRecordInput, graphql_name='input', default=None)),
))
    )
    set_thing_inventory_record_by_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThingInventoryRecordByThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetThingInventoryRecordByThingInput), graphql_name='input', default=None)),
))
    )
    set_thing_schedule_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThingScheduleThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetThingScheduleThing), graphql_name='input', default=None)),
))
    )
    set_thing_spare_part = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThingSparePart', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetThingSparePartInput), graphql_name='input', default=None)),
))
    )
    set_uccform_structure = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='setUCCFormStructure', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(SetUCCFormStructureInput, graphql_name='input', default=None)),
))
    )
    set_uccstack_data = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setUCCStackData', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetUCCStackDataInput), graphql_name='input', default=None)),
))
    )
    set_users_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setUsersThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetUserThingGroupInput), graphql_name='input', default=None)),
))
    )
    set_workbench = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setWorkbench', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='input', default=None)),
))
    )
    sign_up_tenant = sgqlc.types.Field(sgqlc.types.non_null('SignUpTenantInfo'), graphql_name='signUpTenant', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SignUpCompanyTenantInput), graphql_name='input', default=None)),
))
    )
    star_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='starApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(StarAppInput), graphql_name='input', default=None)),
))
    )
    star_pages = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='starPages', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    start_thing_inventory_ticket = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='startThingInventoryTicket', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    submit_change_borrow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='submitChangeBorrow', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    submit_thing_borrow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='submitThingBorrow', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    submit_thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='submitThingCalibrate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    track_thing_inventory_ticket = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='trackThingInventoryTicket', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    transfer_organization = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='transferOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TransferOrganizationInput), graphql_name='input', default=None)),
))
    )
    transfer_tenant_owner = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='transferTenantOwner', args=sgqlc.types.ArgDict((
        ('target_user_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='targetUserId', default=None)),
))
    )
    turn_to_thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='turnToThingCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TurnToThingCalibrateInput), graphql_name='input', default=None)),
))
    )
    turn_to_thing_inspection = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='turnToThingInspection', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TurnToThingInspectionInput), graphql_name='input', default=None)),
))
    )
    turn_to_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='turnToThingMaintenance', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TurnToThingMaintenanceInput), graphql_name='input', default=None)),
))
    )
    turn_to_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='turnToThingRepair', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TurnToThingRepairInput), graphql_name='input', default=None)),
))
    )
    un_assign_app_permissions = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unAssignAppPermissions', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnAssignAppPermissionsInput), graphql_name='input', default=None)),
))
    )
    un_assign_tenant_apps = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unAssignTenantApps', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnAssignTenantAppsInput), graphql_name='input', default=None)),
))
    )
    un_star_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unStarApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnStarAppInput), graphql_name='input', default=None)),
))
    )
    un_star_pages = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unStarPages', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    unbind_email_of_users = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unbindEmailOfUsers', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    unbind_my_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unbindMyEmail', args=sgqlc.types.ArgDict((
        ('verify_code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='verifyCode', default=None)),
))
    )
    unbind_my_phone_number = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unbindMyPhoneNumber', args=sgqlc.types.ArgDict((
        ('verify_code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='verifyCode', default=None)),
))
    )
    unbind_phone_number_of_users = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unbindPhoneNumberOfUsers', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    unbind_wecom_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unbindWecomUser')
    unset_admin_users = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unsetAdminUsers', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    update_account = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateAccount', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateAccountInput), graphql_name='input', default=None)),
))
    )
    update_app_version = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateAppVersion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateAppVersionInput), graphql_name='input', default=None)),
))
    )
    update_authorization_rule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateAuthorizationRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UpdateAuthorizationRuleInput))), graphql_name='input', default=None)),
))
    )
    update_calibrate_organization = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCalibrateOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCalibrateOrganizationInput), graphql_name='input', default=None)),
))
    )
    update_calibrate_schedule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCalibrateSchedule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCalibrateScheduleInput), graphql_name='input', default=None)),
))
    )
    update_change_borrow_approve_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateChangeBorrowApproveConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateChangeBorrowApproveConfigurationInput), graphql_name='input', default=None)),
))
    )
    update_company_thing_category_uccfield = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCompanyThingCategoryUCCField', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCompanyThingCategoryUCCFieldInput), graphql_name='input', default=None)),
))
    )
    update_department_thing_administrator = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateDepartmentThingAdministrator', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateDepartmentThingAdministratorInput), graphql_name='input', default=None)),
))
    )
    update_department_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateDepartmentThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateDepartmentThingGroupInput), graphql_name='input', default=None)),
))
    )
    update_depository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateDepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateDepositoryInput), graphql_name='input', default=None)),
))
    )
    update_eam_field = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateEamField', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEamFieldInput), graphql_name='input', default=None)),
))
    )
    update_eam_spare_part_category = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateEamSparePartCategory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEamSparePartCategoryInput), graphql_name='input', default=None)),
))
    )
    update_eam_spare_part_warehouse = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateEamSparePartWarehouse', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEamSparePartWarehouseInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateEnterpriseApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseAppInput), graphql_name='input', default=None)),
))
    )
    update_evasion_date = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateEvasionDate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEvasionDateInput), graphql_name='input', default=None)),
))
    )
    update_factory = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateFactory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateFactoryInput), graphql_name='input', default=None)),
))
    )
    update_feature_pack = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateFeaturePack', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateFeaturePackInput), graphql_name='input', default=None)),
))
    )
    update_inspection_method = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateInspectionMethod', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateInspectionMethodInput), graphql_name='input', default=None)),
))
    )
    update_maintenance_method = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMaintenanceMethod', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMaintenanceMethodInput), graphql_name='input', default=None)),
))
    )
    update_me = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMe', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMeInput), graphql_name='input', default=None)),
))
    )
    update_meta_channel = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMetaChannel', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMetaChannelInput), graphql_name='input', default=None)),
))
    )
    update_meta_template = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMetaTemplate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMetaTemplateInput), graphql_name='input', default=None)),
))
    )
    update_oauth2_authentication_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateOAuth2AuthenticationConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOAuth2AuthenticationConfigurationInput), graphql_name='input', default=None)),
))
    )
    update_open_idconnect1_authentication_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateOpenIDConnect1AuthenticationConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOpenIDConnect1AuthenticationConfigurationInput), graphql_name='input', default=None)),
))
    )
    update_organization = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOrganizationInput), graphql_name='input', default=None)),
))
    )
    update_outside_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateOutsideCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOutsideCalibrateInput), graphql_name='input', default=None)),
))
    )
    update_role = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateRoleInput), graphql_name='input', default=None)),
))
    )
    update_spare_part = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateSparePart', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateSparePartInput), graphql_name='input', default=None)),
))
    )
    update_spare_part_claim = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateSparePartClaim', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateSparePartClaimInput), graphql_name='input', default=None)),
))
    )
    update_staff = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateStaff', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateStaffInput), graphql_name='input', default=None)),
))
    )
    update_status_of_template = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateStatusOfTemplate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
        ('status', sgqlc.types.Arg(sgqlc.types.non_null(TemplateStatus), graphql_name='status', default=None)),
))
    )
    update_tenant = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateTenant', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTenantInput), graphql_name='input', default=None)),
))
    )
    update_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingInput), graphql_name='input', default=None)),
))
    )
    update_thing_area = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingArea', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingAreaInput), graphql_name='input', default=None)),
))
    )
    update_thing_attachment_type = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingAttachmentType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingAttachmentTypeInput), graphql_name='input', default=None)),
))
    )
    update_thing_bar_label = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingBarLabel', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingBarLabelInput), graphql_name='input', default=None)),
))
    )
    update_thing_borrow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingBorrow', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingBorrowInput), graphql_name='input', default=None)),
))
    )
    update_thing_borrow_approve_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingBorrowApproveConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateThingBorrowApproveConfigurationInput, graphql_name='input', default=None)),
))
    )
    update_thing_borrow_draft_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingBorrowDraftThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingBorrowDraftThingInput), graphql_name='input', default=None)),
))
    )
    update_thing_by_code = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingByCode', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingByCodeInput), graphql_name='input', default=None)),
))
    )
    update_thing_calibrate_operator = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingCalibrateOperator', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingCalibrateOperatorInput), graphql_name='input', default=None)),
))
    )
    update_thing_category = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingCategory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingCategoryInput), graphql_name='input', default=None)),
))
    )
    update_thing_category_uccfield = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingCategoryUCCField', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingCategoryUCCFieldInput), graphql_name='input', default=None)),
))
    )
    update_thing_change_borrow_by_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingChangeBorrowByDraft', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(String, graphql_name='code', default=None)),
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
        ('reason', sgqlc.types.Arg(String, graphql_name='reason', default=None)),
))
    )
    update_thing_change_borrow_draft_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingChangeBorrowDraftThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingChangeBorrowDraftThingInput), graphql_name='input', default=None)),
))
    )
    update_thing_complete_file_rule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingCompleteFileRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingCompleteFileRuleInput), graphql_name='input', default=None)),
))
    )
    update_thing_function_departments = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingFunctionDepartments', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingFunctionDepartmentsInput), graphql_name='input', default=None)),
))
    )
    update_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingGroupInput), graphql_name='input', default=None)),
))
    )
    update_thing_inspection_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingInspectionWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingInspectionWorkflowConfigurationInput), graphql_name='input', default=None)),
))
    )
    update_thing_inventory_redundant_record = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingInventoryRedundantRecord', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingInventoryRedundantRecordInput), graphql_name='input', default=None)),
))
    )
    update_thing_label = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingLabel', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingLabelInput), graphql_name='input', default=None)),
))
    )
    update_thing_maintenance_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingMaintenanceWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingMaintenanceWorkflowConfigurationInput), graphql_name='input', default=None)),
))
    )
    update_thing_repair_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingRepairWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingRepairWorkflowConfigurationInput), graphql_name='input', default=None)),
))
    )
    update_thing_schedule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingSchedule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingScheduleInput), graphql_name='input', default=None)),
))
    )
    update_thing_task = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingTask', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingTaskInput), graphql_name='input', default=None)),
))
    )
    update_thing_ucc = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingUCC', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingUCCInput), graphql_name='input', default=None)),
))
    )
    update_things = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThings', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingsInput), graphql_name='input', default=None)),
))
    )
    update_user_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateUserThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserThingGroupInput), graphql_name='input', default=None)),
))
    )
    update_workflow_base_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateWorkflowBaseConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateWorkflowBaseConfigurationInput), graphql_name='input', default=None)),
))
    )
    use_spare_part_claim = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='useSparePartClaim', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UseSparePartClaimInput), graphql_name='input', default=None)),
))
    )
    visit_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='visitApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    visit_menu = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='visitMenu', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    wecom_app_login = sgqlc.types.Field(sgqlc.types.non_null(AuthInfo), graphql_name='wecomAppLogin', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(LoginInput), graphql_name='input', default=None)),
))
    )
    wecom_login = sgqlc.types.Field(sgqlc.types.non_null(AuthInfo), graphql_name='wecomLogin', args=sgqlc.types.ArgDict((
        ('auth_code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='authCode', default=None)),
))
    )
    writeoff_spare_part_receipt = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='writeoffSparePartReceipt', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(WriteoffSparePartReceiptInput), graphql_name='input', default=None)),
))
    )


class MyBacklogGroup(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('count', 'data', 'group')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Backlog))), graphql_name='data')
    group = sgqlc.types.Field(sgqlc.types.non_null(BacklogGroup), graphql_name='group')


class OldRole(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app', 'created_at', 'desc', 'id', 'name', 'permissions', 'updated_at')
    app = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(App)), graphql_name='app')
    created_at = sgqlc.types.Field(Timestamp, graphql_name='createdAt')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    permissions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Permission'))), graphql_name='permissions')
    updated_at = sgqlc.types.Field(Timestamp, graphql_name='updatedAt')


class OldRoleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(OldRole))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class OperationDetail(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('detail', 'target')
    detail = sgqlc.types.Field(String, graphql_name='detail')
    target = sgqlc.types.Field(String, graphql_name='target')


class Organization(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'current_user_count', 'has_children', 'id', 'is_deleted', 'level', 'manager', 'name', 'parent_id', 'path_name', 'total_user_count')
    code = sgqlc.types.Field(String, graphql_name='code')
    current_user_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='currentUserCount')
    has_children = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasChildren')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    is_deleted = sgqlc.types.Field(Boolean, graphql_name='isDeleted')
    level = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='level')
    manager = sgqlc.types.Field('User', graphql_name='manager')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(String, graphql_name='parentId')
    path_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pathName')
    total_user_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalUserCount')


class OrganizationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Organization))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class OutsideCalibrate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('apply_for_at', 'calibrate_at', 'calibrate_organization', 'id', 'name', 'pay_at', 'pay_status', 'thing_calibrate')
    apply_for_at = sgqlc.types.Field(Timestamp, graphql_name='applyForAt')
    calibrate_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='calibrateAt')
    calibrate_organization = sgqlc.types.Field(sgqlc.types.non_null(CalibrateOrganization), graphql_name='calibrateOrganization')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pay_at = sgqlc.types.Field(Timestamp, graphql_name='payAt')
    pay_status = sgqlc.types.Field(OutsideCalibratePayStatus, graphql_name='payStatus')
    thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='thingCalibrate')


class OutsideCalibrateList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(OutsideCalibrate))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Page(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app', 'avatar', 'id', 'name', 'url')
    app = sgqlc.types.Field(sgqlc.types.non_null(App), graphql_name='app')
    avatar = sgqlc.types.Field(Image, graphql_name='avatar')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class PageList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Page))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Permission(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('apis', 'app', 'data_ranges', 'dependencies', 'id', 'name', 'parent_id', 'path_name', 'type')
    apis = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Api)), graphql_name='apis')
    app = sgqlc.types.Field(sgqlc.types.non_null(App), graphql_name='app')
    data_ranges = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PermissionDataRange')), graphql_name='dataRanges')
    dependencies = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='dependencies')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(String, graphql_name='parentId')
    path_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pathName')
    type = sgqlc.types.Field(sgqlc.types.non_null(PermissionType), graphql_name='type')


class PermissionDataRange(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'name')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Province(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class PushSchedule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('type',)
    type = sgqlc.types.Field(PushScheduleType, graphql_name='type')


class Query(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('log_list', '_eam', 'account', 'account_exists', 'account_list', 'admin_account_list', 'all_authorization_rules_of_role', 'apis', 'app_groups', 'app_menu_list', 'app_version_exists', 'app_version_list', 'assignable_login_modes_of_tenant', 'assignable_meta_template_list_of_tenant', 'assignable_permissions_of_tenant', 'assigned_permissions_of_app', 'authentication_configuration', 'authentication_source', 'authorization_rule_and_dependencies', 'authorization_rule_dependent_by', 'bi_issue_issue', 'calibrate_organization', 'calibrate_organization_list', 'calibrate_schedule', 'calibrate_schedule_list', 'can_replace_thing_list', 'change_borrow', 'change_borrow_approve_configuration', 'change_borrow_approve_configuration_list', 'change_borrow_default_approve_configuration_list', 'change_borrow_item', 'change_borrow_item_list', 'change_borrow_list', 'change_borrow_operator_record_list', 'change_borrow_state_overview', 'check_alter_department_thing_group', 'check_delete_department', 'children_of_department', 'cities', 'city_companies', 'code_rule_configuration', 'companies', 'company_bidatasource_list', 'company_bidatasource_tree', 'company_thing_calibrate_configuration', 'company_thing_category_uccfield', 'company_thing_category_uccfield_list', 'company_thing_department_scope', 'company_thing_group_tree', 'counties', 'countries', 'current_change_borrow_approve_configuration_list', 'current_spare_part_claim_operation_list', 'current_thing_borrow_approve_configuration_list', 'current_thing_borrow_transitions', 'current_thing_calibrate_operation_list', 'current_thing_inspection_workflow_configuration_list', 'current_thing_maintenance_workflow_configuration_list', 'current_thing_repair_workflow_configuration_list', 'department_by_id_and_level', 'department_list', 'department_thing_administrator_list', 'department_thing_groups', 'department_tree', 'dependency_of_permissions', 'depository', 'depository_list', 'dept_user_thing_groups', 'eam_field', 'eam_field_inter_list', 'eam_field_list', 'eam_field_summary', 'eam_file_list', 'eam_form_by_thing_category', 'eam_form_list', 'eam_form_structure', 'eam_spare_part_category', 'eam_spare_part_category_list', 'eam_spare_part_category_tree', 'eam_spare_part_category_tree_nodes', 'eam_spare_part_form_structure', 'eam_spare_part_warehouse', 'eam_spare_part_warehouse_list', 'eam_spare_part_warehouse_manager', 'evasion_date', 'evasion_date_list', 'export_spare_part', 'export_spare_part_claim_list', 'export_spare_part_outbound_list', 'export_spare_part_receipt_list', 'export_spare_part_transfer_list', 'export_thing', 'export_thing_inventory_record', 'export_thing_inventory_track_record', 'factory', 'factory_list', 'feature_pack', 'feature_pack_list', 'feature_pack_subscriptions_of_tenant', 'inbox_message', 'inbox_message_list', 'inspection_method', 'inspection_method_import_template', 'inspection_method_list', 'is_calibrate_organization_exists', 'is_calibrate_schedule_exists', 'is_change_borrow_approve_configuration_exists', 'is_company_thing_category_uccfield_exists', 'is_create_app_version_allowed', 'is_depository_exists', 'is_eam_field_exists', 'is_eam_form_exists', 'is_eam_spare_part_category_exists', 'is_eam_spare_part_warehouse_exists', 'is_email_exists', 'is_email_verified', 'is_exist_thing_circulation', 'is_factory_exists', 'is_feature_pack_exists', 'is_inspection_method_exists', 'is_maintenance_method_exists', 'is_outside_calibrate_exists', 'is_permission_changed_of_latest_app_version', 'is_phone_number_exists', 'is_phone_number_verified', 'is_spare_part_exists', 'is_staff_job_number_exists', 'is_thing_area_code_exists', 'is_thing_area_exists', 'is_thing_attachment_type_exists', 'is_thing_bar_label_exists', 'is_thing_borrow_approve_configuration_exists', 'is_thing_category_code_exists', 'is_thing_category_exists', 'is_thing_category_uccfield_exists', 'is_thing_contain', 'is_thing_exists', 'is_thing_inspection_workflow_configuration_exists', 'is_thing_inventory_ticket_exists', 'is_thing_label_exists', 'is_thing_maintenance_workflow_configuration_exists', 'is_thing_repair_workflow_configuration_exists', 'is_thing_schedule_exists', 'is_thing_uccexists', 'login_config_of_my_tenant', 'login_config_of_tenant_code', 'login_configuration', 'maintenance_method', 'maintenance_method_import_template', 'maintenance_method_list', 'me', 'menu_visit_history_list', 'message_channels_of_tenant', 'message_template_list_of_tenant', 'meta_channels', 'meta_template', 'meta_template_event_exists', 'meta_template_list', 'my_app_list', 'my_backlog_groups', 'my_mobile_app_list', 'my_stared_page', 'my_tenant', 'my_tenant_app_list', 'my_tenant_development_app_list', 'my_tenant_feature_pack_subscriptions', 'my_thing_group', 'my_thing_inventory_record_list', 'organization', 'organization_by_code', 'organization_by_id_and_level', 'organization_code_exists', 'organization_list', 'organization_name_exists_in_siblings', 'organization_tree_nodes', 'outside_calibrate', 'outside_calibrate_list', 'page_list', 'permissions', 'permissions_of_feature_packs', 'permissions_of_tenant', 'provinces', 'recent_app', 'role', 'role_list', 'role_name_exists', 'role_thing_categories', 'root_organization', 'sap_thing_code_history_list', 'spare_part', 'spare_part_claim', 'spare_part_claim_list', 'spare_part_claim_record', 'spare_part_import_template', 'spare_part_list', 'spare_part_outbound', 'spare_part_outbound_item_list', 'spare_part_outbound_list', 'spare_part_outbound_summary', 'spare_part_receipt', 'spare_part_receipt_item_list', 'spare_part_receipt_list', 'spare_part_receipt_writeoff_list', 'spare_part_stock_configuration', 'spare_part_stock_list', 'spare_part_stock_record_list', 'spare_part_transfer', 'spare_part_transfer_item_list', 'spare_part_transfer_list', 'spare_part_usage_record_list', 'spare_part_workflow_configuration', 'spare_part_writeoff_list', 'staff_list', 'stared_apps', 'sub_thing_list', 'sub_thing_ucclist', 'system_log_action', 'system_log_list', 'table_column_setting', 'table_fields_config', 'table_fixed_fields_config', 'tenant', 'tenant_app_list', 'tenant_code_exists', 'tenant_industry_tree_nodes', 'tenant_list', 'tenant_name_exists', 'tenant_uscc_exists', 'thing', 'thing_area', 'thing_area_import_template', 'thing_area_list', 'thing_area_tree', 'thing_attachment_type_list', 'thing_bar_label', 'thing_bar_label_list', 'thing_borrow', 'thing_borrow_approve_configuration', 'thing_borrow_approve_configuration_list', 'thing_borrow_default_approve_configuration_list', 'thing_borrow_draft', 'thing_borrow_list', 'thing_borrow_operator_record_list', 'thing_borrow_range_configuration', 'thing_borrow_relate_resource_list', 'thing_borrow_status_overview', 'thing_borrow_workflow_configuration', 'thing_by_code', 'thing_by_qr_code', 'thing_calibrate', 'thing_calibrate_list', 'thing_calibrate_operator', 'thing_calibrate_operator_department', 'thing_calibrate_operator_list', 'thing_calibrate_range_configuration', 'thing_calibrate_record_list', 'thing_calibrate_workflow_configuration', 'thing_category', 'thing_category_import_template', 'thing_category_list', 'thing_category_tree', 'thing_category_tree_nodes', 'thing_category_uccfield', 'thing_category_uccfield_list', 'thing_change_borrow_draft', 'thing_circulation_list', 'thing_circulation_overview', 'thing_complete_file_rule_list', 'thing_function_department', 'thing_function_department_list', 'thing_group', 'thing_group_depts', 'thing_group_list', 'thing_group_tree', 'thing_group_users', 'thing_import_template', 'thing_inspection', 'thing_inspection_default_workflow_configuration_list', 'thing_inspection_list', 'thing_inspection_operator_record_list', 'thing_inspection_status_overview', 'thing_inspection_workflow_configuration', 'thing_inspection_workflow_configuration_list', 'thing_inventory_record', 'thing_inventory_record_list', 'thing_inventory_redundant_record', 'thing_inventory_redundant_record_list', 'thing_inventory_relate_resource_list', 'thing_inventory_ticket', 'thing_inventory_ticket_list', 'thing_inventory_track_record', 'thing_inventory_track_record_list', 'thing_inventory_track_redundant_record', 'thing_inventory_track_redundant_record_list', 'thing_is_lent_overview', 'thing_label', 'thing_label_import_template', 'thing_label_list', 'thing_list', 'thing_maintenance', 'thing_maintenance_default_workflow_configuration_list', 'thing_maintenance_list', 'thing_maintenance_operator_record_list', 'thing_maintenance_status_overview', 'thing_maintenance_workflow_configuration', 'thing_maintenance_workflow_configuration_list', 'thing_on_state_overview', 'thing_relate_resource_list', 'thing_repair', 'thing_repair_default_workflow_configuration_list', 'thing_repair_list', 'thing_repair_operator_record_list', 'thing_repair_status_overview', 'thing_repair_workflow_configuration', 'thing_repair_workflow_configuration_list', 'thing_schedule', 'thing_schedule_import_template', 'thing_schedule_list', 'thing_schedule_thing_import_template', 'thing_spare_part_import_template', 'thing_task_list', 'thing_transfer_record_list', 'thing_ucc', 'thing_uccby_thing_category', 'thing_ucclist', 'things', 'ucc_form_structure', 'ucc_form_structure_json_schema', 'ucc_stack_data', 'unread_message_apps', 'upload_config', 'upload_configs', 'validate_inspection_method_excel', 'validate_maintenance_method_excel', 'validate_spare_part_excel', 'validate_thing_area_excel', 'validate_thing_category_excel', 'validate_thing_excel', 'validate_thing_label_excel', 'validate_thing_schedule_excel', 'validate_thing_schedule_thing_excel', 'validate_thing_spare_part_excel', 'workbench', 'workbench_card_data', 'workbench_card_option', 'workflow_base_configuration', 'workflow_default_init_state')
    log_list = sgqlc.types.Field(sgqlc.types.non_null('LogList'), graphql_name='LogList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(LogListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    _eam = sgqlc.types.Field(Boolean, graphql_name='_eam')
    account = sgqlc.types.Field(Account, graphql_name='account', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    account_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='accountExists', args=sgqlc.types.ArgDict((
        ('account', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='account', default=None)),
))
    )
    account_list = sgqlc.types.Field(sgqlc.types.non_null(AccountList), graphql_name='accountList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AccountListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    admin_account_list = sgqlc.types.Field(sgqlc.types.non_null(AccountList), graphql_name='adminAccountList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    all_authorization_rules_of_role = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AuthorizationRule))), graphql_name='allAuthorizationRulesOfRole', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AuthorizationRuleFilterInput, graphql_name='filter', default=None)),
        ('role_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='roleId', default=None)),
))
    )
    apis = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Api))), graphql_name='apis', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ApiFilterInput, graphql_name='filter', default=None)),
))
    )
    app_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AppGroup))), graphql_name='appGroups')
    app_menu_list = sgqlc.types.Field(sgqlc.types.non_null(AppMenuList), graphql_name='appMenuList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(MenuListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    app_version_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='appVersionExists', args=sgqlc.types.ArgDict((
        ('app_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='AppId', default=None)),
        ('app_version', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='appVersion', default=None)),
))
    )
    app_version_list = sgqlc.types.Field(sgqlc.types.non_null(AppVersionList), graphql_name='appVersionList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AppVersionListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    assignable_login_modes_of_tenant = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LoginMode))), graphql_name='assignableLoginModesOfTenant', args=sgqlc.types.ArgDict((
        ('tenant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tenantId', default=None)),
))
    )
    assignable_meta_template_list_of_tenant = sgqlc.types.Field(sgqlc.types.non_null(MetaTemplateList), graphql_name='assignableMetaTemplateListOfTenant', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(MetaTemplateListInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('tenant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tenantId', default=None)),
))
    )
    assignable_permissions_of_tenant = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Permission))), graphql_name='assignablePermissionsOfTenant', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(PermissionFilterInput, graphql_name='filter', default=None)),
        ('tenant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tenantId', default=None)),
))
    )
    assigned_permissions_of_app = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Permission))), graphql_name='assignedPermissionsOfApp', args=sgqlc.types.ArgDict((
        ('app_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='appId', default=None)),
))
    )
    authentication_configuration = sgqlc.types.Field(AuthenticationConfiguration, graphql_name='authenticationConfiguration')
    authentication_source = sgqlc.types.Field(AuthenticationSource, graphql_name='authenticationSource', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='companyId', default=None)),
))
    )
    authorization_rule_and_dependencies = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(AuthorizationRule)), graphql_name='authorizationRuleAndDependencies', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    authorization_rule_dependent_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AuthorizationRuleDependentBy))), graphql_name='authorizationRuleDependentBy', args=sgqlc.types.ArgDict((
        ('rule_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ruleIds', default=None)),
        ('user_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='userId', default=None)),
))
    )
    bi_issue_issue = sgqlc.types.Field(sgqlc.types.list_of(BIResult), graphql_name='biIssueIssue', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    calibrate_organization = sgqlc.types.Field(sgqlc.types.non_null(CalibrateOrganization), graphql_name='calibrateOrganization', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    calibrate_organization_list = sgqlc.types.Field(sgqlc.types.non_null(CalibrateOrganizationList), graphql_name='calibrateOrganizationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CalibrateOrganizationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    calibrate_schedule = sgqlc.types.Field(CalibrateSchedule, graphql_name='calibrateSchedule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    calibrate_schedule_list = sgqlc.types.Field(sgqlc.types.non_null(CalibrateScheduleList), graphql_name='calibrateScheduleList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CalibrateScheduleFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    can_replace_thing_list = sgqlc.types.Field(sgqlc.types.non_null('ThingList'), graphql_name='canReplaceThingList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ReplaceThingFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    change_borrow = sgqlc.types.Field(ChangeBorrow, graphql_name='changeBorrow', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    change_borrow_approve_configuration = sgqlc.types.Field(ChangeBorrowApproveConfiguration, graphql_name='changeBorrowApproveConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    change_borrow_approve_configuration_list = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowApproveConfigurationList), graphql_name='changeBorrowApproveConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ChangeBorrowApproveConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    change_borrow_default_approve_configuration_list = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowApproveConfigurationList), graphql_name='changeBorrowDefaultApproveConfigurationList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    change_borrow_item = sgqlc.types.Field(ChangeBorrowItem, graphql_name='changeBorrowItem', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    change_borrow_item_list = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowItemList), graphql_name='changeBorrowItemList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ChangeBorrowItemListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    change_borrow_list = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowList), graphql_name='changeBorrowList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ChangeBorrowListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    change_borrow_operator_record_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ChangeBorrowOperatorRecord))), graphql_name='changeBorrowOperatorRecordList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    change_borrow_state_overview = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowStateOverview), graphql_name='changeBorrowStateOverview', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    check_alter_department_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='checkAlterDepartmentThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CheckAlterDepartmentThingGroupInput), graphql_name='input', default=None)),
))
    )
    check_delete_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='checkDeleteDepartment', args=sgqlc.types.ArgDict((
        ('department', sgqlc.types.Arg(sgqlc.types.non_null(IDInput), graphql_name='department', default=None)),
))
    )
    children_of_department = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Department))), graphql_name='childrenOfDepartment', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='companyId', default=None)),
        ('department_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='departmentId', default=None)),
))
    )
    cities = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(City)), graphql_name='cities', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CityFilterInput, graphql_name='filter', default=None)),
))
    )
    city_companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(City)), graphql_name='cityCompanies')
    code_rule_configuration = sgqlc.types.Field(CodeRuleConfiguration, graphql_name='codeRuleConfiguration', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    companies = sgqlc.types.Field(sgqlc.types.non_null(CompanyList), graphql_name='companies', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyFilter, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    company_bidatasource_list = sgqlc.types.Field(sgqlc.types.non_null(CompanyBIDatasourceList), graphql_name='companyBIDatasourceList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyBIDatasourceFilter, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    company_bidatasource_tree = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(AppBIDatasourceList)), graphql_name='companyBIDatasourceTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyBIDatasourceFilter, graphql_name='filter', default=None)),
))
    )
    company_thing_calibrate_configuration = sgqlc.types.Field('ThingCalibrateConfiguration', graphql_name='companyThingCalibrateConfiguration', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    company_thing_category_uccfield = sgqlc.types.Field(CompanyThingCategoryUCCField, graphql_name='companyThingCategoryUCCField', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    company_thing_category_uccfield_list = sgqlc.types.Field(sgqlc.types.non_null(CompanyThingCategoryUCCFieldList), graphql_name='companyThingCategoryUCCFieldList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyThingCategoryUCCFieldListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    company_thing_department_scope = sgqlc.types.Field(sgqlc.types.non_null(CompanyThingDepartmentScope), graphql_name='companyThingDepartmentScope', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    company_thing_group_tree = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompanyThingGroupNode))), graphql_name='companyThingGroupTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyThingGroupTreeFilterInput, graphql_name='filter', default=None)),
))
    )
    counties = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(County)), graphql_name='counties', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CountyFilterInput, graphql_name='filter', default=None)),
))
    )
    countries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Country)), graphql_name='countries', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(countryFilter, graphql_name='filter', default=None)),
))
    )
    current_change_borrow_approve_configuration_list = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowApproveConfigurationList), graphql_name='currentChangeBorrowApproveConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CurrentChangeBorrowApproveConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    current_spare_part_claim_operation_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SparePartClaimTransitions'))), graphql_name='currentSparePartClaimOperationList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id', default=None)),
))
    )
    current_thing_borrow_approve_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingBorrowApproveConfigurationList'), graphql_name='currentThingBorrowApproveConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CurrentThingBorrowApproveConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    current_thing_borrow_transitions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingBorrowTransitions'))), graphql_name='currentThingBorrowTransitions', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(CurrentThingBorrowTransitionsFilterInput), graphql_name='filter', default=None)),
))
    )
    current_thing_calibrate_operation_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingCalibrateTransitions'))), graphql_name='currentThingCalibrateOperationList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id', default=None)),
))
    )
    current_thing_inspection_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInspectionWorkflowConfigurationList'), graphql_name='currentThingInspectionWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CurrentThingInspectionWorkflowConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    current_thing_maintenance_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenanceWorkflowConfigurationList'), graphql_name='currentThingMaintenanceWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CurrentThingMaintenanceWorkflowConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    current_thing_repair_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingRepairWorkflowConfigurationList'), graphql_name='currentThingRepairWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CurrentThingRepairWorkflowConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    department_by_id_and_level = sgqlc.types.Field(Department, graphql_name='departmentByIdAndLevel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
        ('level', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='level', default=None)),
))
    )
    department_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Department)), graphql_name='departmentList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DepartmentListFilter), graphql_name='filter', default=None)),
))
    )
    department_thing_administrator_list = sgqlc.types.Field(sgqlc.types.non_null(DepartmentThingAdministratorList), graphql_name='departmentThingAdministratorList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(DepartmentThingAdministratorListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    department_thing_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingGroup'))), graphql_name='departmentThingGroups', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(DepartmentThingGroupFilterInput, graphql_name='filter', default=None)),
))
    )
    department_tree = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='departmentTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(DepartmentTreeFilter, graphql_name='filter', default=None)),
))
    )
    dependency_of_permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Permission)), graphql_name='dependencyOfPermissions', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    depository = sgqlc.types.Field(Depository, graphql_name='depository', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    depository_list = sgqlc.types.Field(sgqlc.types.non_null(DepositoryList), graphql_name='depositoryList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(DepositoryListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    dept_user_thing_groups = sgqlc.types.Field(sgqlc.types.non_null('ThingGroupList'), graphql_name='deptUserThingGroups', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DeptUserThingGroupInputFilter), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    eam_field = sgqlc.types.Field(EamField, graphql_name='eamField', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    eam_field_inter_list = sgqlc.types.Field(sgqlc.types.non_null(EamFieldList), graphql_name='eamFieldInterList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(EamFieldInterListFilterInput), graphql_name='filter', default=None)),
))
    )
    eam_field_list = sgqlc.types.Field(sgqlc.types.non_null(EamFieldList), graphql_name='eamFieldList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(EamFieldListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    eam_field_summary = sgqlc.types.Field(sgqlc.types.non_null(EamFieldSummary), graphql_name='eamFieldSummary', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    eam_file_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EamFile))), graphql_name='eamFileList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(EamFileListFilterInput), graphql_name='filter', default=None)),
))
    )
    eam_form_by_thing_category = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EamFormStructure))), graphql_name='eamFormByThingCategory', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(EamFormByThingCategoryFilterInput), graphql_name='filter', default=None)),
))
    )
    eam_form_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EamFormStructure))), graphql_name='eamFormList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(EamFormListFilterInput, graphql_name='filter', default=None)),
))
    )
    eam_form_structure = sgqlc.types.Field(sgqlc.types.non_null(EamFormStructure), graphql_name='eamFormStructure', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(EamFormStructureFilter), graphql_name='filter', default=None)),
))
    )
    eam_spare_part_category = sgqlc.types.Field(EamSparePartCategory, graphql_name='eamSparePartCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    eam_spare_part_category_list = sgqlc.types.Field(sgqlc.types.non_null(EamSparePartCategoryList), graphql_name='eamSparePartCategoryList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(EamSparePartCategoryListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    eam_spare_part_category_tree = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='eamSparePartCategoryTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(EamSparePartCategoryListFilterInput), graphql_name='filter', default=None)),
))
    )
    eam_spare_part_category_tree_nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(EamSparePartCategory)), graphql_name='eamSparePartCategoryTreeNodes', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(EamSparePartCategoryListFilterInput, graphql_name='filter', default=None)),
))
    )
    eam_spare_part_form_structure = sgqlc.types.Field(sgqlc.types.non_null(EamSparePartFormStructure), graphql_name='eamSparePartFormStructure', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(EamSparePartFormStructureFilter), graphql_name='filter', default=None)),
))
    )
    eam_spare_part_warehouse = sgqlc.types.Field(EamSparePartWarehouse, graphql_name='eamSparePartWarehouse', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    eam_spare_part_warehouse_list = sgqlc.types.Field(sgqlc.types.non_null(EamSparePartWarehouseList), graphql_name='eamSparePartWarehouseList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(EamSparePartWarehouseListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    eam_spare_part_warehouse_manager = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='eamSparePartWarehouseManager', args=sgqlc.types.ArgDict((
        ('warehouse', sgqlc.types.Arg(sgqlc.types.non_null(IntIDInput), graphql_name='warehouse', default=None)),
))
    )
    evasion_date = sgqlc.types.Field(EvasionDate, graphql_name='evasionDate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    evasion_date_list = sgqlc.types.Field(sgqlc.types.non_null(EvasionDateList), graphql_name='evasionDateList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(EvasionDateFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    export_spare_part = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportSparePart', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartFilterInput, graphql_name='filter', default=None)),
        ('table_fields_config', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ExcelTableFieldConfigInput))), graphql_name='tableFieldsConfig', default=None)),
))
    )
    export_spare_part_claim_list = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportSparePartClaimList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartClaimListFilterInput, graphql_name='filter', default=None)),
))
    )
    export_spare_part_outbound_list = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportSparePartOutboundList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartOutboundFilterInput, graphql_name='filter', default=None)),
))
    )
    export_spare_part_receipt_list = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportSparePartReceiptList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartReceiptFilterInput, graphql_name='filter', default=None)),
))
    )
    export_spare_part_transfer_list = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportSparePartTransferList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartTransferFilterInput, graphql_name='filter', default=None)),
))
    )
    export_thing = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportThing', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingFilterInput, graphql_name='filter', default=None)),
        ('table_fields_config', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ExcelTableFieldConfigInput))), graphql_name='tableFieldsConfig', default=None)),
))
    )
    export_thing_inventory_record = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportThingInventoryRecord', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingInventoryRecordListFilterInput, graphql_name='filter', default=None)),
))
    )
    export_thing_inventory_track_record = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportThingInventoryTrackRecord', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingInventoryTrackRecordListFilterInput, graphql_name='filter', default=None)),
        ('table_fields_config', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ExcelTableFieldConfigInput))), graphql_name='tableFieldsConfig', default=None)),
))
    )
    factory = sgqlc.types.Field(Factory, graphql_name='factory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    factory_list = sgqlc.types.Field(sgqlc.types.non_null(FactoryList), graphql_name='factoryList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(FactoryListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    feature_pack = sgqlc.types.Field(FeaturePack, graphql_name='featurePack', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    feature_pack_list = sgqlc.types.Field(sgqlc.types.non_null(FeaturePackList), graphql_name='featurePackList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(FeaturePackListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    feature_pack_subscriptions_of_tenant = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FeaturePackSubscription))), graphql_name='featurePackSubscriptionsOfTenant', args=sgqlc.types.ArgDict((
        ('tenant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tenantId', default=None)),
))
    )
    inbox_message = sgqlc.types.Field(sgqlc.types.non_null(InboxMessage), graphql_name='inboxMessage', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    inbox_message_list = sgqlc.types.Field(sgqlc.types.non_null(InboxMessageList), graphql_name='inboxMessageList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(InboxMessageFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    inspection_method = sgqlc.types.Field(InspectionMethod, graphql_name='inspectionMethod', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    inspection_method_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='inspectionMethodImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    inspection_method_list = sgqlc.types.Field(sgqlc.types.non_null(InspectionMethodList), graphql_name='inspectionMethodList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(InspectionMethodListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    is_calibrate_organization_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCalibrateOrganizationExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsCalibrateOrganizationInput), graphql_name='input', default=None)),
))
    )
    is_calibrate_schedule_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCalibrateScheduleExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsCalibrateScheduleExistsInput), graphql_name='input', default=None)),
))
    )
    is_change_borrow_approve_configuration_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isChangeBorrowApproveConfigurationExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsChangeBorrowApproveConfigurationExists), graphql_name='input', default=None)),
))
    )
    is_company_thing_category_uccfield_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCompanyThingCategoryUCCFieldExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsCompanyThingCategoryUCCFieldExistsInput), graphql_name='input', default=None)),
))
    )
    is_create_app_version_allowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCreateAppVersionAllowed', args=sgqlc.types.ArgDict((
        ('app_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='appId', default=None)),
))
    )
    is_depository_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDepositoryExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsDepositoryExistsInput), graphql_name='input', default=None)),
))
    )
    is_eam_field_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEamFieldExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsEamFieldExistsFilterInput), graphql_name='input', default=None)),
))
    )
    is_eam_form_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEamFormExists', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(IsEamFormExistsFilterInput), graphql_name='filter', default=None)),
))
    )
    is_eam_spare_part_category_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEamSparePartCategoryExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsEamSparePartCategoryExistsInput), graphql_name='input', default=None)),
))
    )
    is_eam_spare_part_warehouse_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEamSparePartWarehouseExists', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(IsEamSparePartWarehouseExistsFilter), graphql_name='filter', default=None)),
))
    )
    is_email_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEmailExists', args=sgqlc.types.ArgDict((
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
))
    )
    is_email_verified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEmailVerified', args=sgqlc.types.ArgDict((
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
))
    )
    is_exist_thing_circulation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isExistThingCirculation', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(IsExistThingCirculationFilterInput), graphql_name='filter', default=None)),
))
    )
    is_factory_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFactoryExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsFactoryExistsInput), graphql_name='input', default=None)),
))
    )
    is_feature_pack_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFeaturePackExists', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    is_inspection_method_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isInspectionMethodExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsInspectionMethodExistsInput), graphql_name='input', default=None)),
))
    )
    is_maintenance_method_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMaintenanceMethodExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsMaintenanceMethodExistsInput), graphql_name='input', default=None)),
))
    )
    is_outside_calibrate_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isOutsideCalibrateExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsOutsideCalibrateExistsInput), graphql_name='input', default=None)),
))
    )
    is_permission_changed_of_latest_app_version = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPermissionChangedOfLatestAppVersion', args=sgqlc.types.ArgDict((
        ('app_id', sgqlc.types.Arg(String, graphql_name='appId', default=None)),
))
    )
    is_phone_number_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPhoneNumberExists', args=sgqlc.types.ArgDict((
        ('phone_number', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='phoneNumber', default=None)),
))
    )
    is_phone_number_verified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPhoneNumberVerified', args=sgqlc.types.ArgDict((
        ('phone_number', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='phoneNumber', default=None)),
))
    )
    is_spare_part_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSparePartExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsSparePartExistsInput), graphql_name='input', default=None)),
))
    )
    is_staff_job_number_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isStaffJobNumberExists', args=sgqlc.types.ArgDict((
        ('job_number', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='jobNumber', default=None)),
))
    )
    is_thing_area_code_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingAreaCodeExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingAreaCodeExistsInput), graphql_name='input', default=None)),
))
    )
    is_thing_area_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingAreaExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingAreaExistsInput), graphql_name='input', default=None)),
))
    )
    is_thing_attachment_type_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingAttachmentTypeExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsAttachmentTypeListExistsInput), graphql_name='input', default=None)),
))
    )
    is_thing_bar_label_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingBarLabelExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingBarLabelExistsInput), graphql_name='input', default=None)),
))
    )
    is_thing_borrow_approve_configuration_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingBorrowApproveConfigurationExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingBorrowApproveConfigurationExists), graphql_name='input', default=None)),
))
    )
    is_thing_category_code_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingCategoryCodeExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingCategoryCodeExistsInput), graphql_name='input', default=None)),
))
    )
    is_thing_category_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingCategoryExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingCategoryExistsInput), graphql_name='input', default=None)),
))
    )
    is_thing_category_uccfield_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingCategoryUCCFieldExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingCategoryUCCFieldExistsInput), graphql_name='input', default=None)),
))
    )
    is_thing_contain = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingContain', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingContainInput), graphql_name='input', default=None)),
))
    )
    is_thing_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingExistsInput), graphql_name='input', default=None)),
))
    )
    is_thing_inspection_workflow_configuration_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingInspectionWorkflowConfigurationExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(IsThingInspectionWorkflowConfigurationExists, graphql_name='input', default=None)),
))
    )
    is_thing_inventory_ticket_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingInventoryTicketExists', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(IsThingInventoryTicketExistsInput), graphql_name='filter', default=None)),
))
    )
    is_thing_label_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingLabelExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingLabelExistsInput), graphql_name='input', default=None)),
))
    )
    is_thing_maintenance_workflow_configuration_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingMaintenanceWorkflowConfigurationExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(IsThingMaintenanceWorkflowConfigurationExists, graphql_name='input', default=None)),
))
    )
    is_thing_repair_workflow_configuration_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingRepairWorkflowConfigurationExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(IsThingRepairWorkflowConfigurationExists, graphql_name='input', default=None)),
))
    )
    is_thing_schedule_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingScheduleExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingScheduleExistsInput), graphql_name='input', default=None)),
))
    )
    is_thing_uccexists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingUCCExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingUCCExistsInput), graphql_name='input', default=None)),
))
    )
    login_config_of_my_tenant = sgqlc.types.Field(sgqlc.types.non_null(LoginConfig), graphql_name='loginConfigOfMyTenant')
    login_config_of_tenant_code = sgqlc.types.Field(sgqlc.types.non_null(LoginConfig), graphql_name='loginConfigOfTenantCode', args=sgqlc.types.ArgDict((
        ('tenant_code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tenantCode', default=None)),
))
    )
    login_configuration = sgqlc.types.Field(sgqlc.types.non_null(LoginConfiguration), graphql_name='loginConfiguration', args=sgqlc.types.ArgDict((
        ('tenant_code', sgqlc.types.Arg(String, graphql_name='tenantCode', default=None)),
        ('tenant_id', sgqlc.types.Arg(String, graphql_name='tenantId', default=None)),
))
    )
    maintenance_method = sgqlc.types.Field(MaintenanceMethod, graphql_name='maintenanceMethod', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    maintenance_method_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='maintenanceMethodImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    maintenance_method_list = sgqlc.types.Field(sgqlc.types.non_null(MaintenanceMethodList), graphql_name='maintenanceMethodList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(MaintenanceMethodListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    me = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='me')
    menu_visit_history_list = sgqlc.types.Field(sgqlc.types.non_null(MenuVisitHistoryList), graphql_name='menuVisitHistoryList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(MenuVisitHistoryListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    message_channels_of_tenant = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MessageChannel))), graphql_name='messageChannelsOfTenant', args=sgqlc.types.ArgDict((
        ('tenant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tenantId', default=None)),
))
    )
    message_template_list_of_tenant = sgqlc.types.Field(sgqlc.types.non_null(MessageTemplateList), graphql_name='messageTemplateListOfTenant', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(MessageTemplateListInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('tenant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tenantId', default=None)),
))
    )
    meta_channels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MetaChannel))), graphql_name='metaChannels')
    meta_template = sgqlc.types.Field(sgqlc.types.non_null(MetaTemplate), graphql_name='metaTemplate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    meta_template_event_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='metaTemplateEventExists', args=sgqlc.types.ArgDict((
        ('event', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='event', default=None)),
))
    )
    meta_template_list = sgqlc.types.Field(sgqlc.types.non_null(MetaTemplateList), graphql_name='metaTemplateList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(MetaTemplateListInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    my_app_list = sgqlc.types.Field(sgqlc.types.non_null(AppList), graphql_name='myAppList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    my_backlog_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MyBacklogGroup))), graphql_name='myBacklogGroups', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(MyBacklogGroupFilterInput, graphql_name='filter', default=None)),
))
    )
    my_mobile_app_list = sgqlc.types.Field(sgqlc.types.non_null(AppList), graphql_name='myMobileAppList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    my_stared_page = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Page))), graphql_name='myStaredPage', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(PageListFilterInput, graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    my_tenant = sgqlc.types.Field(sgqlc.types.non_null('Tenant'), graphql_name='myTenant')
    my_tenant_app_list = sgqlc.types.Field(sgqlc.types.non_null(AppList), graphql_name='myTenantAppList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(MyTenantAppListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    my_tenant_development_app_list = sgqlc.types.Field(sgqlc.types.non_null(AppList), graphql_name='myTenantDevelopmentAppList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(MyTenantDevelopmentAppListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    my_tenant_feature_pack_subscriptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FeaturePackSubscription))), graphql_name='myTenantFeaturePackSubscriptions')
    my_thing_group = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='myThingGroup', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyId', default=None)),
))
    )
    my_thing_inventory_record_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInventoryRecordList'), graphql_name='myThingInventoryRecordList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(MyThingInventoryRecordListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    organization = sgqlc.types.Field(Organization, graphql_name='organization', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    organization_by_code = sgqlc.types.Field(Organization, graphql_name='organizationByCode', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    organization_by_id_and_level = sgqlc.types.Field(Organization, graphql_name='organizationByIdAndLevel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
        ('level', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='level', default=None)),
))
    )
    organization_code_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='organizationCodeExists', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    organization_list = sgqlc.types.Field(sgqlc.types.non_null(OrganizationList), graphql_name='organizationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(OrganizationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    organization_name_exists_in_siblings = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='organizationNameExistsInSiblings', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('parent_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='parentId', default=None)),
))
    )
    organization_tree_nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Organization))), graphql_name='organizationTreeNodes', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(OrganizationTreeNodeFilterInput, graphql_name='filter', default=None)),
))
    )
    outside_calibrate = sgqlc.types.Field(OutsideCalibrate, graphql_name='outsideCalibrate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    outside_calibrate_list = sgqlc.types.Field(sgqlc.types.non_null(OutsideCalibrateList), graphql_name='outsideCalibrateList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(OutsideCalibrateListListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    page_list = sgqlc.types.Field(sgqlc.types.non_null(PageList), graphql_name='pageList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(PageListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Permission)), graphql_name='permissions', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(PermissionFilterInput, graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    permissions_of_feature_packs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Permission))), graphql_name='permissionsOfFeaturePacks', args=sgqlc.types.ArgDict((
        ('feature_pack_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='featurePackIds', default=None)),
        ('filter', sgqlc.types.Arg(PermissionFilterInput, graphql_name='filter', default=None)),
))
    )
    permissions_of_tenant = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Permission))), graphql_name='permissionsOfTenant', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(PermissionFilterInput, graphql_name='filter', default=None)),
        ('tenant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tenantId', default=None)),
))
    )
    provinces = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Province)), graphql_name='provinces')
    recent_app = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(App))), graphql_name='recentApp', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=None)),
))
    )
    role = sgqlc.types.Field('Role', graphql_name='role', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    role_list = sgqlc.types.Field(sgqlc.types.non_null('RoleList'), graphql_name='roleList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(RoleFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    role_name_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='roleNameExists', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    role_thing_categories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingCategory'))), graphql_name='roleThingCategories', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(RoleThingCategoryFilterInput, graphql_name='filter', default=None)),
))
    )
    root_organization = sgqlc.types.Field(sgqlc.types.non_null(Organization), graphql_name='rootOrganization')
    sap_thing_code_history_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SapThingCodeHistory'))), graphql_name='sapThingCodeHistoryList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    spare_part = sgqlc.types.Field('SparePart', graphql_name='sparePart', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    spare_part_claim = sgqlc.types.Field('SparePartClaim', graphql_name='sparePartClaim', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    spare_part_claim_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartClaimList'), graphql_name='sparePartClaimList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartClaimListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    spare_part_claim_record = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SparePartClaimRecord'))), graphql_name='sparePartClaimRecord', args=sgqlc.types.ArgDict((
        ('claim', sgqlc.types.Arg(IntIDInput, graphql_name='claim', default=None)),
))
    )
    spare_part_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='sparePartImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    spare_part_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartList'), graphql_name='sparePartList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    spare_part_outbound = sgqlc.types.Field('SparePartOutbound', graphql_name='sparePartOutbound', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    spare_part_outbound_item_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartOutboundItemList'), graphql_name='sparePartOutboundItemList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(SparePartOutboundItemFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    spare_part_outbound_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartOutboundList'), graphql_name='sparePartOutboundList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartOutboundFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    spare_part_outbound_summary = sgqlc.types.Field(sgqlc.types.non_null('SparePartOutboundSummary'), graphql_name='sparePartOutboundSummary', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartOutboundSummaryFilterInput, graphql_name='filter', default=None)),
))
    )
    spare_part_receipt = sgqlc.types.Field('SparePartReceipt', graphql_name='sparePartReceipt', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    spare_part_receipt_item_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartReceiptItemList'), graphql_name='sparePartReceiptItemList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(SparePartReceiptItemFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    spare_part_receipt_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartReceiptList'), graphql_name='sparePartReceiptList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartReceiptFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    spare_part_receipt_writeoff_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartReceiptWriteoffList'), graphql_name='sparePartReceiptWriteoffList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(SparePartReceiptWriteoffFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    spare_part_stock_configuration = sgqlc.types.Field('SparePartStockConfiguration', graphql_name='sparePartStockConfiguration')
    spare_part_stock_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartStockList'), graphql_name='sparePartStockList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartStockFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    spare_part_stock_record_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartStockRecordList'), graphql_name='sparePartStockRecordList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(SparePartStockRecordFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    spare_part_transfer = sgqlc.types.Field('SparePartTransfer', graphql_name='sparePartTransfer', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    spare_part_transfer_item_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartTransferItemList'), graphql_name='sparePartTransferItemList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(SparePartTransferItemFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    spare_part_transfer_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartTransferList'), graphql_name='sparePartTransferList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartTransferFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    spare_part_usage_record_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartUsageRecordList'), graphql_name='sparePartUsageRecordList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(SparePartUsageRecordFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    spare_part_workflow_configuration = sgqlc.types.Field('SparePartWorkflowConfiguration', graphql_name='sparePartWorkflowConfiguration')
    spare_part_writeoff_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartWriteoffList'), graphql_name='sparePartWriteoffList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartWriteoffFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    staff_list = sgqlc.types.Field(sgqlc.types.non_null('StaffList'), graphql_name='staffList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(StaffListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    stared_apps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(App))), graphql_name='staredApps')
    sub_thing_list = sgqlc.types.Field(sgqlc.types.non_null('ThingList'), graphql_name='subThingList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SubThingListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    sub_thing_ucclist = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingUCC'))), graphql_name='subThingUCCList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(SubThingUccListFilterInput), graphql_name='filter', default=None)),
))
    )
    system_log_action = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='systemLogAction', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyId', default=None)),
))
    )
    system_log_list = sgqlc.types.Field(sgqlc.types.non_null('SystemLogList'), graphql_name='systemLogList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(SystemLogFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    table_column_setting = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TableColumn'))), graphql_name='tableColumnSetting', args=sgqlc.types.ArgDict((
        ('default_columns', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TableColumnInput))), graphql_name='defaultColumns', default=None)),
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
))
    )
    table_fields_config = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TableFieldConfig'))), graphql_name='tableFieldsConfig', args=sgqlc.types.ArgDict((
        ('default_fields_config', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TableFieldConfigInput))), graphql_name='defaultFieldsConfig', default=None)),
        ('filter', sgqlc.types.Arg(TableFieldConfigFilterInput, graphql_name='filter', default=None)),
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
))
    )
    table_fixed_fields_config = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TableFixedField'))), graphql_name='tableFixedFieldsConfig', args=sgqlc.types.ArgDict((
        ('default_fields_config', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TableFixedFieldInput))), graphql_name='defaultFieldsConfig', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(TableFixedFieldsConfigFilterInput), graphql_name='filter', default=None)),
))
    )
    tenant = sgqlc.types.Field('Tenant', graphql_name='tenant', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    tenant_app_list = sgqlc.types.Field(sgqlc.types.non_null(AppList), graphql_name='tenantAppList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(TenantAppListFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    tenant_code_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='tenantCodeExists', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    tenant_industry_tree_nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TenantIndustry'))), graphql_name='tenantIndustryTreeNodes', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(TenantIndustryTreeNodeFilterInput, graphql_name='filter', default=None)),
))
    )
    tenant_list = sgqlc.types.Field(sgqlc.types.non_null('TenantList'), graphql_name='tenantList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(TenantFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    tenant_name_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='tenantNameExists', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    tenant_uscc_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='tenantUsccExists', args=sgqlc.types.ArgDict((
        ('uscc', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='uscc', default=None)),
))
    )
    thing = sgqlc.types.Field('Thing', graphql_name='thing', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    thing_area = sgqlc.types.Field('ThingArea', graphql_name='thingArea', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_area_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='thingAreaImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_area_list = sgqlc.types.Field(sgqlc.types.non_null('ThingAreaList'), graphql_name='thingAreaList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingAreaListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_area_tree = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='thingAreaTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingAreaListFilterInput), graphql_name='filter', default=None)),
))
    )
    thing_attachment_type_list = sgqlc.types.Field(sgqlc.types.non_null('ThingAttachmentTypeList'), graphql_name='thingAttachmentTypeList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingAttachmentTypeListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_bar_label = sgqlc.types.Field('ThingBarLabel', graphql_name='thingBarLabel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_bar_label_list = sgqlc.types.Field(sgqlc.types.non_null('ThingBarLabelList'), graphql_name='thingBarLabelList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingBarLabelListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_borrow = sgqlc.types.Field('ThingBorrow', graphql_name='thingBorrow', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_borrow_approve_configuration = sgqlc.types.Field('ThingBorrowApproveConfiguration', graphql_name='thingBorrowApproveConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_borrow_approve_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingBorrowApproveConfigurationList'), graphql_name='thingBorrowApproveConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingBorrowApproveConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_borrow_default_approve_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingBorrowApproveConfigurationList'), graphql_name='thingBorrowDefaultApproveConfigurationList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_borrow_draft = sgqlc.types.Field('ThingBorrowDraft', graphql_name='thingBorrowDraft', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_borrow_list = sgqlc.types.Field(sgqlc.types.non_null('ThingBorrowList'), graphql_name='thingBorrowList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingBorrowListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_borrow_operator_record_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingBorrowOperatorRecord'))), graphql_name='thingBorrowOperatorRecordList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_borrow_range_configuration = sgqlc.types.Field('ThingBorrowRangeConfiguration', graphql_name='thingBorrowRangeConfiguration', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IntIDInput, graphql_name='company', default=None)),
))
    )
    thing_borrow_relate_resource_list = sgqlc.types.Field(sgqlc.types.non_null('ThingBorrowRelateResourceList'), graphql_name='thingBorrowRelateResourceList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingBorrowRelateResourceListFilterInput), graphql_name='filter', default=None)),
))
    )
    thing_borrow_status_overview = sgqlc.types.Field(sgqlc.types.non_null('ThingBorrowStatusOverview'), graphql_name='thingBorrowStatusOverview', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_borrow_workflow_configuration = sgqlc.types.Field('ThingBorrowWorkflowConfiguration', graphql_name='thingBorrowWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IntIDInput, graphql_name='company', default=None)),
))
    )
    thing_by_code = sgqlc.types.Field('Thing', graphql_name='thingByCode', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    thing_by_qr_code = sgqlc.types.Field('Thing', graphql_name='thingByQrCode', args=sgqlc.types.ArgDict((
        ('qr_code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='qrCode', default=None)),
))
    )
    thing_calibrate = sgqlc.types.Field('ThingCalibrate', graphql_name='thingCalibrate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_calibrate_list = sgqlc.types.Field(sgqlc.types.non_null('ThingCalibrateList'), graphql_name='thingCalibrateList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingCalibrateListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_calibrate_operator = sgqlc.types.Field('ThingCalibrateOperator', graphql_name='thingCalibrateOperator', args=sgqlc.types.ArgDict((
        ('user', sgqlc.types.Arg(sgqlc.types.non_null(StringIDInput), graphql_name='user', default=None)),
))
    )
    thing_calibrate_operator_department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Department)), graphql_name='thingCalibrateOperatorDepartment')
    thing_calibrate_operator_list = sgqlc.types.Field('ThingCalibrateOperatorList', graphql_name='thingCalibrateOperatorList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingCalibrateOperatorListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_calibrate_range_configuration = sgqlc.types.Field('ThingCalibrateRangeConfiguration', graphql_name='thingCalibrateRangeConfiguration')
    thing_calibrate_record_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingCalibrateRecord'))), graphql_name='thingCalibrateRecordList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_calibrate_workflow_configuration = sgqlc.types.Field('ThingCalibrateWorkflowConfiguration', graphql_name='thingCalibrateWorkflowConfiguration')
    thing_category = sgqlc.types.Field('ThingCategory', graphql_name='thingCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_category_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='thingCategoryImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_category_list = sgqlc.types.Field(sgqlc.types.non_null('ThingCategoryList'), graphql_name='thingCategoryList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingCategoryListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_category_tree = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='thingCategoryTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingCategoryListFilterInput), graphql_name='filter', default=None)),
))
    )
    thing_category_tree_nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ThingCategory')), graphql_name='thingCategoryTreeNodes', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingCategoryListFilterInput, graphql_name='filter', default=None)),
))
    )
    thing_category_uccfield = sgqlc.types.Field('ThingCategoryUCCField', graphql_name='thingCategoryUCCField', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_category_uccfield_list = sgqlc.types.Field(sgqlc.types.non_null('ThingCategoryUCCFieldList'), graphql_name='thingCategoryUCCFieldList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingCategoryUCCFieldListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_change_borrow_draft = sgqlc.types.Field('ThingChangeBorrowDraft', graphql_name='thingChangeBorrowDraft', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_circulation_list = sgqlc.types.Field(sgqlc.types.non_null('ThingCirculationList'), graphql_name='thingCirculationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingCirculationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_circulation_overview = sgqlc.types.Field(sgqlc.types.non_null('ThingCirculationOverview'), graphql_name='thingCirculationOverview', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_complete_file_rule_list = sgqlc.types.Field(sgqlc.types.non_null('ThingCompleteFileRuleList'), graphql_name='thingCompleteFileRuleList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingCompleteFileRuleListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_function_department = sgqlc.types.Field('ThingFunctionDepartment', graphql_name='thingFunctionDepartment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_function_department_list = sgqlc.types.Field(sgqlc.types.non_null('ThingFunctionDepartmentList'), graphql_name='thingFunctionDepartmentList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingFunctionDepartmentFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_group = sgqlc.types.Field(sgqlc.types.non_null('ThingGroup'), graphql_name='thingGroup', args=sgqlc.types.ArgDict((
        ('thing_group', sgqlc.types.Arg(sgqlc.types.non_null(IDInput), graphql_name='thingGroup', default=None)),
))
    )
    thing_group_depts = sgqlc.types.Field(sgqlc.types.non_null(DeptThingGroupList), graphql_name='thingGroupDepts', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingGroupDeptFilter), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    thing_group_list = sgqlc.types.Field(sgqlc.types.non_null('ThingGroupList'), graphql_name='thingGroupList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingGroupFilter, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    thing_group_tree = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='thingGroupTree', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(Int, graphql_name='companyId', default=None)),
))
    )
    thing_group_users = sgqlc.types.Field(sgqlc.types.non_null('UserThingGroupList'), graphql_name='thingGroupUsers', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingGroupUserFilter), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    thing_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='thingImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_inspection = sgqlc.types.Field('ThingInspection', graphql_name='thingInspection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_inspection_default_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInspectionWorkflowConfigurationList'), graphql_name='thingInspectionDefaultWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_inspection_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInspectionList'), graphql_name='thingInspectionList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingInspectionListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_inspection_operator_record_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInspectionOperatorRecordList'), graphql_name='thingInspectionOperatorRecordList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_inspection_status_overview = sgqlc.types.Field(sgqlc.types.non_null('ThingInspectionStatusOverview'), graphql_name='thingInspectionStatusOverview', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_inspection_workflow_configuration = sgqlc.types.Field('ThingInspectionWorkflowConfiguration', graphql_name='thingInspectionWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_inspection_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInspectionWorkflowConfigurationList'), graphql_name='thingInspectionWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingInspectionWorkflowConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_inventory_record = sgqlc.types.Field('ThingInventoryRecord', graphql_name='thingInventoryRecord', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_inventory_record_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInventoryRecordList'), graphql_name='thingInventoryRecordList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingInventoryRecordListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_inventory_redundant_record = sgqlc.types.Field('ThingInventoryRedundantRecord', graphql_name='thingInventoryRedundantRecord', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_inventory_redundant_record_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInventoryRedundantRecordList'), graphql_name='thingInventoryRedundantRecordList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingInventoryRedundantRecordListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_inventory_relate_resource_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInventoryRelateResourceList'), graphql_name='thingInventoryRelateResourceList')
    thing_inventory_ticket = sgqlc.types.Field('ThingInventoryTicket', graphql_name='thingInventoryTicket', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_inventory_ticket_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInventoryTicketList'), graphql_name='thingInventoryTicketList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingInventoryTicketListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_inventory_track_record = sgqlc.types.Field('ThingInventoryTrackRecord', graphql_name='thingInventoryTrackRecord', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_inventory_track_record_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInventoryTrackRecordList'), graphql_name='thingInventoryTrackRecordList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingInventoryTrackRecordListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_inventory_track_redundant_record = sgqlc.types.Field('ThingInventoryTrackRedundantRecord', graphql_name='thingInventoryTrackRedundantRecord', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_inventory_track_redundant_record_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInventoryTrackRedundantRecordList'), graphql_name='thingInventoryTrackRedundantRecordList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingInventoryTrackRedundantRecordListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_is_lent_overview = sgqlc.types.Field(sgqlc.types.non_null('ThingIsLentOverview'), graphql_name='thingIsLentOverview', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(Int, graphql_name='companyId', default=None)),
))
    )
    thing_label = sgqlc.types.Field('ThingLabel', graphql_name='thingLabel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_label_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='thingLabelImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_label_list = sgqlc.types.Field(sgqlc.types.non_null('ThingLabelList'), graphql_name='thingLabelList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingLabelListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_list = sgqlc.types.Field(sgqlc.types.non_null('ThingList'), graphql_name='thingList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_maintenance = sgqlc.types.Field('ThingMaintenance', graphql_name='thingMaintenance', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_maintenance_default_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenanceWorkflowConfigurationList'), graphql_name='thingMaintenanceDefaultWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_maintenance_list = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenanceList'), graphql_name='thingMaintenanceList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingMaintenanceFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_maintenance_operator_record_list = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenanceOperatorRecordList'), graphql_name='thingMaintenanceOperatorRecordList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_maintenance_status_overview = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenanceStatusOverview'), graphql_name='thingMaintenanceStatusOverview', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_maintenance_workflow_configuration = sgqlc.types.Field('ThingMaintenanceWorkflowConfiguration', graphql_name='thingMaintenanceWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_maintenance_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenanceWorkflowConfigurationList'), graphql_name='thingMaintenanceWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingMaintenanceWorkflowConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_on_state_overview = sgqlc.types.Field(sgqlc.types.non_null('ThingOnStateOverview'), graphql_name='thingOnStateOverview', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(Int, graphql_name='companyId', default=None)),
))
    )
    thing_relate_resource_list = sgqlc.types.Field('ThingRelateResourceList', graphql_name='thingRelateResourceList')
    thing_repair = sgqlc.types.Field('ThingRepair', graphql_name='thingRepair', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_repair_default_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingRepairWorkflowConfigurationList'), graphql_name='thingRepairDefaultWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_repair_list = sgqlc.types.Field(sgqlc.types.non_null('ThingRepairList'), graphql_name='thingRepairList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingRepairFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_repair_operator_record_list = sgqlc.types.Field(sgqlc.types.non_null('ThingRepairOperatorRecordList'), graphql_name='thingRepairOperatorRecordList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_repair_status_overview = sgqlc.types.Field(sgqlc.types.non_null('ThingRepairStatusOverview'), graphql_name='thingRepairStatusOverview', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_repair_workflow_configuration = sgqlc.types.Field('ThingRepairWorkflowConfiguration', graphql_name='thingRepairWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_repair_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingRepairWorkflowConfigurationList'), graphql_name='thingRepairWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingRepairWorkflowConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_schedule = sgqlc.types.Field('ThingSchedule', graphql_name='thingSchedule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_schedule_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='thingScheduleImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_schedule_list = sgqlc.types.Field(sgqlc.types.non_null('ThingScheduleList'), graphql_name='thingScheduleList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingScheduleFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_schedule_thing_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='thingScheduleThingImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_spare_part_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='thingSparePartImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_task_list = sgqlc.types.Field(sgqlc.types.non_null('ThingTaskList'), graphql_name='thingTaskList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingTaskFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_transfer_record_list = sgqlc.types.Field(sgqlc.types.non_null('ThingTransferRecordList'), graphql_name='thingTransferRecordList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingTransferRecordListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_ucc = sgqlc.types.Field('ThingUCC', graphql_name='thingUCC', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
))
    )
    thing_uccby_thing_category = sgqlc.types.Field('ThingUCC', graphql_name='thingUCCByThingCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_ucclist = sgqlc.types.Field(sgqlc.types.non_null('ThingUCCList'), graphql_name='thingUCCList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingUCCListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    things = sgqlc.types.Field(sgqlc.types.non_null('ThingList'), graphql_name='things', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    ucc_form_structure = sgqlc.types.Field(sgqlc.types.non_null('UCCFormStructure'), graphql_name='uccFormStructure', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(UCCFormStructureFilter), graphql_name='filter', default=None)),
))
    )
    ucc_form_structure_json_schema = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='uccFormStructureJsonSchema', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(UCCFormStructureFilter), graphql_name='filter', default=None)),
))
    )
    ucc_stack_data = sgqlc.types.Field(JSON, graphql_name='uccStackData', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(uccStackDataFilter), graphql_name='filter', default=None)),
))
    )
    unread_message_apps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(App))), graphql_name='unreadMessageApps')
    upload_config = sgqlc.types.Field('UploadConfig', graphql_name='uploadConfig', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    upload_configs = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UploadConfig')), graphql_name='uploadConfigs', args=sgqlc.types.ArgDict((
        ('names', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='names', default=None)),
))
    )
    validate_inspection_method_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateInspectionMethodExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    validate_maintenance_method_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateMaintenanceMethodExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    validate_spare_part_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateSparePartExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    validate_thing_area_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateThingAreaExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    validate_thing_category_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateThingCategoryExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    validate_thing_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateThingExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    validate_thing_label_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateThingLabelExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    validate_thing_schedule_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateThingScheduleExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    validate_thing_schedule_thing_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateThingScheduleThingExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    validate_thing_spare_part_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateThingSparePartExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    workbench = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkbenchCard'))), graphql_name='workbench')
    workbench_card_data = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='workbenchCardData', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    workbench_card_option = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkbenchCard'))), graphql_name='workbenchCardOption')
    workflow_base_configuration = sgqlc.types.Field('WorkflowBaseConfiguration', graphql_name='workflowBaseConfiguration', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    workflow_default_init_state = sgqlc.types.Field(sgqlc.types.non_null('WorkflowDefaultInitState'), graphql_name='workflowDefaultInitState')


class RawFile(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'name')
    data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='data')
    name = sgqlc.types.Field(String, graphql_name='name')


class RenderStyle(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('config', 'kind', 'meta_channel_id')
    config = sgqlc.types.Field(JSON, graphql_name='config')
    kind = sgqlc.types.Field(MessageKind, graphql_name='kind')
    meta_channel_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='meta_channel_id')


class RepairSparePartItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'spare_part', 'spare_part_outbound')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null('SparePart'), graphql_name='sparePart')
    spare_part_outbound = sgqlc.types.Field(sgqlc.types.non_null('SparePartOutbound'), graphql_name='sparePartOutbound')


class Repeat(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('day_of_month', 'day_of_week', 'day_of_year', 'frequency', 'period')
    day_of_month = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dayOfMonth')
    day_of_week = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dayOfWeek')
    day_of_year = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DayOfYear)), graphql_name='dayOfYear')
    frequency = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='frequency')
    period = sgqlc.types.Field(sgqlc.types.non_null(RepeatPeriod), graphql_name='period')


class Role(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('authorization_rules', 'created_at', 'description', 'id', 'name', 'updated_at', 'user_count')
    authorization_rules = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AuthorizationRule))), graphql_name='authorizationRules')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')
    user_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='userCount')


class RoleAuthorizationRule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('authorization_rule_id', 'id', 'role_id')
    authorization_rule_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='authorization_rule_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    role_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='role_id')


class RoleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Role))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SapThingCodeHistory(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('created_at', 'id', 'sap_code_after', 'sap_code_before')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    sap_code_after = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sapCodeAfter')
    sap_code_before = sgqlc.types.Field(String, graphql_name='sapCodeBefore')


class SignUpTenantInfo(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('account', 'auth_info', 'email', 'name', 'password', 'phone', 'tenant_code')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    auth_info = sgqlc.types.Field(sgqlc.types.non_null(AuthInfo), graphql_name='authInfo')
    email = sgqlc.types.Field(String, graphql_name='email')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    tenant_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tenantCode')


class SparePart(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'category', 'code', 'distributor', 'field_data', 'id', 'inventory', 'inventory_total', 'manufacturer', 'model', 'name', 'remark', 'safe_inventory_max', 'safe_inventory_min', 'specification', 'thing')
    attachment = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EamFile))), graphql_name='attachment')
    category = sgqlc.types.Field(EamSparePartCategory, graphql_name='category')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    inventory = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SparePartInventory')), graphql_name='inventory')
    inventory_total = sgqlc.types.Field(Int, graphql_name='inventoryTotal')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    model = sgqlc.types.Field(String, graphql_name='model')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    safe_inventory_max = sgqlc.types.Field(Int, graphql_name='safeInventoryMax')
    safe_inventory_min = sgqlc.types.Field(Int, graphql_name='safeInventoryMin')
    specification = sgqlc.types.Field(String, graphql_name='specification')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Thing')), graphql_name='thing')


class SparePartClaim(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'created_by', 'date', 'department', 'id', 'item', 'reason', 'remark', 'status', 'warehouse')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    created_by = sgqlc.types.Field('User', graphql_name='createdBy')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    department = sgqlc.types.Field(Department, graphql_name='department')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SparePartClaimItem'))), graphql_name='item')
    reason = sgqlc.types.Field(sgqlc.types.non_null(SparePartClaimReason), graphql_name='reason')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    status = sgqlc.types.Field(sgqlc.types.non_null(SparePartClaimStatus), graphql_name='status')
    warehouse = sgqlc.types.Field(sgqlc.types.non_null(EamSparePartWarehouse), graphql_name='warehouse')


class SparePartClaimItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('confirm', 'issue', 'quantity', 'spare_part', 'usage', 'warehouse')
    confirm = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='confirm')
    issue = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='issue')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(SparePart), graphql_name='sparePart')
    usage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='usage')
    warehouse = sgqlc.types.Field(sgqlc.types.non_null(EamSparePartWarehouse), graphql_name='warehouse')


class SparePartClaimList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartClaim))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartClaimRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('created_at', 'created_by', 'msg', 'operate_type', 'outbound')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    created_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createdBy')
    msg = sgqlc.types.Field(String, graphql_name='msg')
    operate_type = sgqlc.types.Field(sgqlc.types.non_null(SparePartClaimOperatorType), graphql_name='operateType')
    outbound = sgqlc.types.Field('SparePartOutbound', graphql_name='outbound')


class SparePartClaimTransitions(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('operator', 'spare_part_claim_id')
    operator = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartClaimOperatorType))), graphql_name='operator')
    spare_part_claim_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='sparePartClaimId')


class SparePartInventory(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'warehouse')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    warehouse = sgqlc.types.Field(sgqlc.types.non_null(EamSparePartWarehouse), graphql_name='warehouse')


class SparePartList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePart))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartOutbound(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('claim', 'code', 'created_by', 'date', 'id', 'item', 'kind', 'operator', 'remark', 'transfer', 'warehouse')
    claim = sgqlc.types.Field(SparePartClaim, graphql_name='claim')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    created_by = sgqlc.types.Field('User', graphql_name='createdBy')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SparePartOutboundItem'))), graphql_name='item')
    kind = sgqlc.types.Field(sgqlc.types.non_null(SparePartOutboundKind), graphql_name='kind')
    operator = sgqlc.types.Field('User', graphql_name='operator')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    transfer = sgqlc.types.Field('SparePartTransfer', graphql_name='transfer')
    warehouse = sgqlc.types.Field(sgqlc.types.non_null(EamSparePartWarehouse), graphql_name='warehouse')


class SparePartOutboundItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_confirmed', 'quantity', 'spare_part')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_confirmed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isConfirmed')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(SparePart), graphql_name='sparePart')


class SparePartOutboundItemList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartOutboundItem))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartOutboundList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartOutbound))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartOutboundSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartOutboundItem))), graphql_name='data')


class SparePartReceipt(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'created_by', 'date', 'id', 'item', 'kind', 'remark', 'warehouse')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    created_by = sgqlc.types.Field('User', graphql_name='createdBy')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SparePartReceiptItem'))), graphql_name='item')
    kind = sgqlc.types.Field(sgqlc.types.non_null(SparePartReceiptKind), graphql_name='kind')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    warehouse = sgqlc.types.Field(sgqlc.types.non_null(EamSparePartWarehouse), graphql_name='warehouse')


class SparePartReceiptItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'spare_part', 'writeoff')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(SparePart), graphql_name='sparePart')
    writeoff = sgqlc.types.Field(Int, graphql_name='writeoff')


class SparePartReceiptItemList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartReceiptItem))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartReceiptList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartReceipt))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartReceiptWriteoffList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SparePartReceiptWriteoffRecord'))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartReceiptWriteoffRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('created_at', 'created_by', 'quantity', 'reason', 'spare_part')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    created_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createdBy')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    reason = sgqlc.types.Field(String, graphql_name='reason')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(SparePart), graphql_name='sparePart')


class SparePartReview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('assignee', 'default_review_operate', 'enabled', 'level')
    assignee = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='assignee')
    default_review_operate = sgqlc.types.Field(SparePartDefaultReviewOperate, graphql_name='defaultReviewOperate')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    level = sgqlc.types.Field(EamWorkflowReviewerLevel, graphql_name='level')


class SparePartStock(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'spare_part', 'warehouse')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(SparePart), graphql_name='sparePart')
    warehouse = sgqlc.types.Field(sgqlc.types.non_null(EamSparePartWarehouse), graphql_name='warehouse')


class SparePartStockConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('role', 'scope')
    role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Role)), graphql_name='role')
    scope = sgqlc.types.Field(sgqlc.types.non_null(SparePartStockScope), graphql_name='scope')


class SparePartStockList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartStock))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartStockRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('created_at', 'outbound', 'receipt', 'type', 'warehouse')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    outbound = sgqlc.types.Field(SparePartOutbound, graphql_name='outbound')
    receipt = sgqlc.types.Field(SparePartReceipt, graphql_name='receipt')
    type = sgqlc.types.Field(sgqlc.types.non_null(SparePartStockRecordType), graphql_name='type')
    warehouse = sgqlc.types.Field(sgqlc.types.non_null(EamSparePartWarehouse), graphql_name='warehouse')


class SparePartStockRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartStockRecord))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartSwitch(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('enabled',)
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')


class SparePartTransfer(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'created_by', 'date', 'export', 'id', 'import_', 'item', 'remark')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    created_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createdBy')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    export = sgqlc.types.Field(sgqlc.types.non_null(EamSparePartWarehouse), graphql_name='export')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    import_ = sgqlc.types.Field(sgqlc.types.non_null(EamSparePartWarehouse), graphql_name='import')
    item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SparePartTransferItem'))), graphql_name='item')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class SparePartTransferItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'quantity', 'spare_part')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(SparePart), graphql_name='sparePart')


class SparePartTransferItemList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartTransferItem))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartTransferList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartTransfer))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartUsageRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('created_at', 'created_by', 'quantity', 'spare_part', 'thing')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    created_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createdBy')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(SparePart), graphql_name='sparePart')
    thing = sgqlc.types.Field(sgqlc.types.non_null('Thing'), graphql_name='thing')


class SparePartUsageRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartUsageRecord))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartWorkflowConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('under_confirm', 'under_issue', 'under_review')
    under_confirm = sgqlc.types.Field(sgqlc.types.non_null(SparePartSwitch), graphql_name='underConfirm')
    under_issue = sgqlc.types.Field(sgqlc.types.non_null(SparePartSwitch), graphql_name='underIssue')
    under_review = sgqlc.types.Field(sgqlc.types.non_null(SparePartReview), graphql_name='underReview')


class SparePartWriteoff(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'date', 'depository', 'id', 'item', 'kind', 'reason', 'spare_part_outbound', 'spare_part_receipt')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    depository = sgqlc.types.Field(sgqlc.types.non_null(Depository), graphql_name='depository')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SparePartWriteoffItem'))), graphql_name='item')
    kind = sgqlc.types.Field(sgqlc.types.non_null(SparePartWriteoffKind), graphql_name='kind')
    reason = sgqlc.types.Field(String, graphql_name='reason')
    spare_part_outbound = sgqlc.types.Field(SparePartOutbound, graphql_name='sparePartOutbound')
    spare_part_receipt = sgqlc.types.Field(SparePartReceipt, graphql_name='sparePartReceipt')


class SparePartWriteoffItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'quantity', 'spare_part', 'spare_part_outbound_item', 'spare_part_receipt_item')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(SparePart), graphql_name='sparePart')
    spare_part_outbound_item = sgqlc.types.Field(SparePartOutboundItem, graphql_name='sparePartOutboundItem')
    spare_part_receipt_item = sgqlc.types.Field(SparePartReceiptItem, graphql_name='sparePartReceiptItem')


class SparePartWriteoffList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartWriteoff))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Staff(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('account', 'avatar', 'created_at', 'email', 'id', 'job_number', 'job_status', 'job_type', 'name', 'organizations', 'phone_number', 'remark', 'tenant', 'updated_at')
    account = sgqlc.types.Field(Account, graphql_name='account')
    avatar = sgqlc.types.Field(Image, graphql_name='avatar')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    job_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='jobNumber')
    job_status = sgqlc.types.Field(sgqlc.types.non_null(StaffJobStatus), graphql_name='jobStatus')
    job_type = sgqlc.types.Field(sgqlc.types.non_null(StaffJobType), graphql_name='jobType')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    organizations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Organization))), graphql_name='organizations')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    tenant = sgqlc.types.Field(sgqlc.types.non_null('Tenant'), graphql_name='tenant')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class StaffList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Staff))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SystemLog(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('action', 'app', 'id', 'resource', 'timestamp', 'user')
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    app = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='app')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    resource = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='resource')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    user = sgqlc.types.Field('User', graphql_name='user')


class SystemLogList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SystemLog))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TableColumn(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('disabled', 'fixed', 'name', 'unchecked')
    disabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='disabled')
    fixed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='fixed')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    unchecked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unchecked')


class TableConfig(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('fields', 'key', 'label')
    fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TableFieldConfig'))), graphql_name='fields')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')


class TableFieldConfig(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('editable', 'fixed', 'key', 'label', 'visible')
    editable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='editable')
    fixed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='fixed')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    visible = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='visible')


class TableFixedField(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('disabled', 'hide', 'label', 'meta', 'name', 'options', 'required')
    disabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='disabled')
    hide = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hide')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    meta = sgqlc.types.Field(sgqlc.types.non_null('TableFixedFieldMeta'), graphql_name='meta')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    options = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TableFixedFieldOption')), graphql_name='options')
    required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='required')


class TableFixedFieldMeta(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('can_config', 'can_disabled', 'can_hide', 'can_required', 'desc', 'group_name', 'label', 'options')
    can_config = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canConfig')
    can_disabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canDisabled')
    can_hide = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canHide')
    can_required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canRequired')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    group_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='groupName')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    options = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TableFixedFieldOption')), graphql_name='options')


class TableFixedFieldOption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('label', 'value')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class TempFile(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('length', 'name', 'url')
    length = sgqlc.types.Field(Int, graphql_name='length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class Tenant(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('address', 'business_license_image', 'certification_failed_reason', 'certification_status', 'city', 'code', 'company_id', 'county', 'created_at', 'email', 'feature_pack_subscriptions', 'id', 'industry', 'is_certification_result_notified', 'name', 'owner', 'phone', 'province', 'status', 'type', 'uscc')
    address = sgqlc.types.Field(String, graphql_name='address')
    business_license_image = sgqlc.types.Field(Image, graphql_name='businessLicenseImage')
    certification_failed_reason = sgqlc.types.Field(String, graphql_name='certificationFailedReason')
    certification_status = sgqlc.types.Field(sgqlc.types.non_null(TenantCertificationStatus), graphql_name='certificationStatus')
    city = sgqlc.types.Field(sgqlc.types.non_null(City), graphql_name='city')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='companyId')
    county = sgqlc.types.Field(sgqlc.types.non_null(County), graphql_name='county')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    email = sgqlc.types.Field(String, graphql_name='email')
    feature_pack_subscriptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FeaturePackSubscription))), graphql_name='featurePackSubscriptions')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    industry = sgqlc.types.Field(sgqlc.types.non_null('TenantIndustry'), graphql_name='industry')
    is_certification_result_notified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCertificationResultNotified')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    owner = sgqlc.types.Field('User', graphql_name='owner')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(sgqlc.types.non_null(Province), graphql_name='province')
    status = sgqlc.types.Field(sgqlc.types.non_null(TenantStatus), graphql_name='status')
    type = sgqlc.types.Field(sgqlc.types.non_null(TenantType), graphql_name='type')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')


class TenantApp(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app_id', 'id', 'tenant_id')
    app_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='appId')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    tenant_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tenantId')


class TenantIndustry(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'parent_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(String, graphql_name='parentId')


class TenantList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Tenant))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Thing(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('acceptance_at', 'account_type', 'accounting_department', 'activated_at', 'alert_at', 'apply_for_purchase_at', 'apply_for_purchase_num', 'area', 'arrived_at', 'asset_normalization_at', 'attachment', 'book_value', 'brand', 'calibrate_code', 'calibrate_method', 'calibrate_repeat', 'calibrate_result', 'calibrate_state', 'can_borrowed', 'can_calibrate', 'can_operate_borrowed', 'category', 'code', 'code_prefix', 'company_id', 'contract_num', 'department', 'depreciation_of_year', 'depreciation_rate', 'depreciation_rate_of_month', 'desc', 'distributor', 'field_data', 'final_value', 'fuselage_code', 'group_file', 'id', 'image', 'installed_at', 'is_calibration_expired', 'is_complete_file', 'is_deleted', 'is_lent', 'label', 'last_calibrate_at', 'lease_begin_at', 'lease_finish_at', 'lease_num', 'machine_number', 'maintainer', 'manager', 'manufacturer', 'model_num', 'name', 'next_calibrate_at', 'on_state', 'parent_thing_id', 'performance_status', 'po_num', 'predict_residual_rate', 'produce_at', 'purchase_price', 'purchase_type', 'purchased_at', 'qr_code', 'sap_thing_code', 'serial_number', 'spare_part', 'specification', 'storage_addr', 'storage_type', 'sub_thing_id', 'thing_group', 'thing_subject_code', 'transfer_at', 'transfer_record', 'used_year', 'warranty_deadline_at', 'warranty_institutions', 'warranty_method', 'years_of_use')
    acceptance_at = sgqlc.types.Field(Timestamp, graphql_name='acceptanceAt')
    account_type = sgqlc.types.Field(ThingAccountType, graphql_name='accountType')
    accounting_department = sgqlc.types.Field(Department, graphql_name='accountingDepartment')
    activated_at = sgqlc.types.Field(Timestamp, graphql_name='activatedAt')
    alert_at = sgqlc.types.Field(Timestamp, graphql_name='alertAt')
    apply_for_purchase_at = sgqlc.types.Field(Timestamp, graphql_name='applyForPurchaseAt')
    apply_for_purchase_num = sgqlc.types.Field(String, graphql_name='applyForPurchaseNum')
    area = sgqlc.types.Field('ThingArea', graphql_name='area')
    arrived_at = sgqlc.types.Field(Timestamp, graphql_name='arrivedAt')
    asset_normalization_at = sgqlc.types.Field(Timestamp, graphql_name='assetNormalizationAt')
    attachment = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EamFile))), graphql_name='attachment')
    book_value = sgqlc.types.Field(Float, graphql_name='bookValue')
    brand = sgqlc.types.Field(String, graphql_name='brand')
    calibrate_code = sgqlc.types.Field(String, graphql_name='calibrateCode')
    calibrate_method = sgqlc.types.Field(sgqlc.types.non_null(CalibrateMethod), graphql_name='calibrateMethod')
    calibrate_repeat = sgqlc.types.Field(CalibrateRepeat, graphql_name='calibrateRepeat')
    calibrate_result = sgqlc.types.Field(sgqlc.types.non_null(CalibrateResult), graphql_name='calibrateResult')
    calibrate_state = sgqlc.types.Field(sgqlc.types.non_null(CalibrateState), graphql_name='calibrateState')
    can_borrowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canBorrowed')
    can_calibrate = sgqlc.types.Field(Boolean, graphql_name='canCalibrate')
    can_operate_borrowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canOperateBorrowed')
    category = sgqlc.types.Field('ThingCategory', graphql_name='category')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    code_prefix = sgqlc.types.Field(CodePrefix, graphql_name='codePrefix')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='companyID')
    contract_num = sgqlc.types.Field(String, graphql_name='contractNum')
    department = sgqlc.types.Field(Department, graphql_name='department')
    depreciation_of_year = sgqlc.types.Field(Float, graphql_name='depreciationOfYear')
    depreciation_rate = sgqlc.types.Field(Float, graphql_name='depreciationRate')
    depreciation_rate_of_month = sgqlc.types.Field(Float, graphql_name='depreciationRateOfMonth')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    final_value = sgqlc.types.Field(Float, graphql_name='finalValue')
    fuselage_code = sgqlc.types.Field(String, graphql_name='fuselageCode')
    group_file = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GroupFile))), graphql_name='groupFile')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EamFile))), graphql_name='image')
    installed_at = sgqlc.types.Field(Timestamp, graphql_name='installedAt')
    is_calibration_expired = sgqlc.types.Field(Boolean, graphql_name='isCalibrationExpired')
    is_complete_file = sgqlc.types.Field(Boolean, graphql_name='isCompleteFile')
    is_deleted = sgqlc.types.Field(Boolean, graphql_name='isDeleted')
    is_lent = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLent')
    label = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingLabel'))), graphql_name='label')
    last_calibrate_at = sgqlc.types.Field(Timestamp, graphql_name='lastCalibrateAt')
    lease_begin_at = sgqlc.types.Field(Timestamp, graphql_name='leaseBeginAt')
    lease_finish_at = sgqlc.types.Field(Timestamp, graphql_name='leaseFinishAt')
    lease_num = sgqlc.types.Field(String, graphql_name='leaseNum')
    machine_number = sgqlc.types.Field(String, graphql_name='machineNumber')
    maintainer = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='maintainer')
    manager = sgqlc.types.Field('User', graphql_name='manager')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    model_num = sgqlc.types.Field(String, graphql_name='modelNum')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    next_calibrate_at = sgqlc.types.Field(Timestamp, graphql_name='nextCalibrateAt')
    on_state = sgqlc.types.Field(sgqlc.types.non_null(OnState), graphql_name='onState')
    parent_thing_id = sgqlc.types.Field(ID, graphql_name='parentThingId')
    performance_status = sgqlc.types.Field(ThingPerformanceStatus, graphql_name='performanceStatus')
    po_num = sgqlc.types.Field(String, graphql_name='poNum')
    predict_residual_rate = sgqlc.types.Field(Float, graphql_name='predictResidualRate')
    produce_at = sgqlc.types.Field(Timestamp, graphql_name='produceAt')
    purchase_price = sgqlc.types.Field(Float, graphql_name='purchasePrice')
    purchase_type = sgqlc.types.Field(ThingPurchaseType, graphql_name='purchaseType')
    purchased_at = sgqlc.types.Field(Timestamp, graphql_name='purchasedAt')
    qr_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='qrCode')
    sap_thing_code = sgqlc.types.Field(String, graphql_name='sapThingCode')
    serial_number = sgqlc.types.Field(String, graphql_name='serialNumber')
    spare_part = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePart)), graphql_name='sparePart')
    specification = sgqlc.types.Field(String, graphql_name='specification')
    storage_addr = sgqlc.types.Field(String, graphql_name='storageAddr')
    storage_type = sgqlc.types.Field(ThingStorageType, graphql_name='storageType')
    sub_thing_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='subThingId')
    thing_group = sgqlc.types.Field('ThingGroup', graphql_name='thingGroup')
    thing_subject_code = sgqlc.types.Field(String, graphql_name='thingSubjectCode')
    transfer_at = sgqlc.types.Field(Timestamp, graphql_name='transferAt')
    transfer_record = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingTransferRecord'))), graphql_name='transferRecord')
    used_year = sgqlc.types.Field(Float, graphql_name='usedYear')
    warranty_deadline_at = sgqlc.types.Field(Timestamp, graphql_name='warrantyDeadlineAt')
    warranty_institutions = sgqlc.types.Field(String, graphql_name='warrantyInstitutions')
    warranty_method = sgqlc.types.Field(ThingWarrantyMethod, graphql_name='warrantyMethod')
    years_of_use = sgqlc.types.Field(Float, graphql_name='yearsOfUse')


class ThingArea(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'id', 'name', 'parent_id')
    code = sgqlc.types.Field(String, graphql_name='code')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(Int, graphql_name='parentId')


class ThingAreaList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingArea))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingAttachmentType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class ThingAttachmentTypeList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingAttachmentType))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingBarLabel(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('activate_bar_code', 'activate_field', 'activate_logo', 'bar_code_type', 'board_layout', 'field_key', 'font_size', 'height', 'id', 'logo', 'name', 'preview_image', 'show_bar_code', 'width')
    activate_bar_code = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='activateBarCode')
    activate_field = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='activateField')
    activate_logo = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='activateLogo')
    bar_code_type = sgqlc.types.Field(BarCodeType, graphql_name='barCodeType')
    board_layout = sgqlc.types.Field(JSON, graphql_name='boardLayout')
    field_key = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fieldKey')
    font_size = sgqlc.types.Field(Float, graphql_name='fontSize')
    height = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='height')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    logo = sgqlc.types.Field(EamFile, graphql_name='logo')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    preview_image = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='previewImage')
    show_bar_code = sgqlc.types.Field(Boolean, graphql_name='showBarCode')
    width = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='width')


class ThingBarLabelList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingBarLabel))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingBorrow(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('applicant', 'attachment', 'created_at', 'department_of_applicant', 'expected', 'id', 'operator', 'reason', 'state', 'status', 'thing', 'updated_at')
    applicant = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='applicant')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EamFile)), graphql_name='attachment')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    department_of_applicant = sgqlc.types.Field(Department, graphql_name='departmentOfApplicant')
    expected = sgqlc.types.Field(sgqlc.types.non_null(TimestampRange), graphql_name='expected')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field('User', graphql_name='operator')
    reason = sgqlc.types.Field(String, graphql_name='reason')
    state = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowState), graphql_name='state')
    status = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowStatus), graphql_name='status')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class ThingBorrowApproveConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowState), graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowState), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowTrigger), graphql_name='trigger')


class ThingBorrowApproveConfigurationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingBorrowApproveConfiguration))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingBorrowDraft(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'data', 'id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingBorrowDraftData'))), graphql_name='data')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class ThingBorrowDraftData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('expected_borrow_at', 'expected_return_at', 'thing')
    expected_borrow_at = sgqlc.types.Field(Timestamp, graphql_name='expectedBorrowAt')
    expected_return_at = sgqlc.types.Field(Timestamp, graphql_name='expectedReturnAt')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')


class ThingBorrowEvaluation(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('assignee', 'default_review_operate', 'enabled', 'rule')
    assignee = sgqlc.types.Field('User', graphql_name='assignee')
    default_review_operate = sgqlc.types.Field(EamWorkflowDefaultReviewOperate, graphql_name='defaultReviewOperate')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    rule = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingBorrowEvaluationRule')), graphql_name='rule')


class ThingBorrowEvaluationRule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('assignee', 'department', 'name', 'thing_category')
    assignee = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='assignee')
    department = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Department))), graphql_name='department')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_category = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingCategory'))), graphql_name='thingCategory')


class ThingBorrowList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingBorrow))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingBorrowLostConfirmation(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('enabled',)
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')


class ThingBorrowOperatorRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'created_at', 'id', 'operate_type', 'operator', 'opinion', 'state')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EamFile)), graphql_name='attachment')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operate_type = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowOperatorType), graphql_name='operateType')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    opinion = sgqlc.types.Field(String, graphql_name='opinion')
    state = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowState), graphql_name='state')


class ThingBorrowRangeConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('department', 'exclude', 'include', 'is_multiple', 'thing_category')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Department)), graphql_name='department')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Thing)), graphql_name='exclude')
    include = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Thing)), graphql_name='include')
    is_multiple = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMultiple')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingCategory')), graphql_name='thingCategory')


class ThingBorrowRelateResourceList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('applicant', 'department_of_applicant', 'operator')
    applicant = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='applicant')
    department_of_applicant = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Department)), graphql_name='departmentOfApplicant')
    operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='operator')


class ThingBorrowReview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('assignee', 'default_review_operate', 'enabled', 'level', 'reviewer')
    assignee = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='assignee')
    default_review_operate = sgqlc.types.Field(EamWorkflowDefaultReviewOperate, graphql_name='defaultReviewOperate')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    level = sgqlc.types.Field(EamWorkflowReviewerLevel, graphql_name='level')
    reviewer = sgqlc.types.Field(EamWorkflowReviewer, graphql_name='reviewer')


class ThingBorrowStatusOverview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('lent_count', 'lost_count', 'pending_count', 'returned_count', 'total_count', 'under_review_count', 'withdraw_count')
    lent_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='lentCount')
    lost_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='lostCount')
    pending_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pendingCount')
    returned_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='returnedCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    under_review_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='underReviewCount')
    withdraw_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='withdrawCount')


class ThingBorrowTransitions(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('operator', 'thing_borrow_id')
    operator = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingBorrowOperatorType))), graphql_name='operator')
    thing_borrow_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='thingBorrowId')


class ThingBorrowWorkflowConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('borrow_evaluation', 'lost_confirmation', 'return_evaluation', 'under_review_by_apply_for', 'under_review_by_borrowed')
    borrow_evaluation = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowEvaluation), graphql_name='borrowEvaluation')
    lost_confirmation = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowLostConfirmation), graphql_name='lostConfirmation')
    return_evaluation = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowEvaluation), graphql_name='returnEvaluation')
    under_review_by_apply_for = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowReview), graphql_name='underReviewByApplyFor')
    under_review_by_borrowed = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowReview), graphql_name='underReviewByBorrowed')


class ThingCalibrate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('calibrate_at', 'calibrate_label', 'calibrate_method', 'calibrate_organization', 'calibrate_report', 'calibrate_result', 'certificate_return_at', 'code', 'created_at', 'deadline', 'explain', 'id', 'operator', 'reason', 'return_at', 'send_at', 'state', 'status', 'thing', 'thing_repair', 'updated_at')
    calibrate_at = sgqlc.types.Field(Timestamp, graphql_name='calibrateAt')
    calibrate_label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EamFile)), graphql_name='calibrateLabel')
    calibrate_method = sgqlc.types.Field(CalibrateMethod, graphql_name='calibrateMethod')
    calibrate_organization = sgqlc.types.Field(CalibrateOrganization, graphql_name='calibrateOrganization')
    calibrate_report = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EamFile)), graphql_name='calibrateReport')
    calibrate_result = sgqlc.types.Field(CalibrateResult, graphql_name='calibrateResult')
    certificate_return_at = sgqlc.types.Field(Timestamp, graphql_name='certificateReturnAt')
    code = sgqlc.types.Field(String, graphql_name='code')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    deadline = sgqlc.types.Field(Timestamp, graphql_name='deadline')
    explain = sgqlc.types.Field(String, graphql_name='explain')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field('User', graphql_name='operator')
    reason = sgqlc.types.Field(sgqlc.types.non_null(CalibrateReason), graphql_name='reason')
    return_at = sgqlc.types.Field(Timestamp, graphql_name='returnAt')
    send_at = sgqlc.types.Field(Timestamp, graphql_name='sendAt')
    state = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateState), graphql_name='state')
    status = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateStatus), graphql_name='status')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')
    thing_repair = sgqlc.types.Field('ThingRepair', graphql_name='thingRepair')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class ThingCalibrateConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('by_thing_repair', 'id')
    by_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='byThingRepair')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class ThingCalibrateList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingCalibrate))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingCalibrateOperator(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('department', 'user')
    department = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Department))), graphql_name='department')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')


class ThingCalibrateOperatorList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingCalibrateOperator))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingCalibratePending(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('assignee',)
    assignee = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='assignee')


class ThingCalibrateRangeConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('thing_category',)
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingCategory')), graphql_name='thingCategory')


class ThingCalibrateRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'created_at', 'id', 'operator', 'operator_record_type', 'remark', 'state', 'turn_to')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EamFile)), graphql_name='attachment')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    operator_record_type = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateOperatorType), graphql_name='operatorRecordType')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    state = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateState), graphql_name='state')
    turn_to = sgqlc.types.Field('User', graphql_name='turnTo')


class ThingCalibrateReview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('assignee', 'default_review_operate', 'level', 'reviewer')
    assignee = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='assignee')
    default_review_operate = sgqlc.types.Field(EamWorkflowDefaultReviewOperate, graphql_name='defaultReviewOperate')
    level = sgqlc.types.Field(EamWorkflowReviewerLevel, graphql_name='level')
    reviewer = sgqlc.types.Field(EamWorkflowReviewer, graphql_name='reviewer')


class ThingCalibrateTransitions(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('operator', 'thing_calibrate_id')
    operator = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingCalibrateOperatorType))), graphql_name='operator')
    thing_calibrate_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='thingCalibrateId')


class ThingCalibrateWorkflowConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('pending', 'under_review')
    pending = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibratePending), graphql_name='pending')
    under_review = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateReview), graphql_name='underReview')


class ThingCategory(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'id', 'is_calibration', 'name', 'parent_id', 'path_info', 'ucc_field', 'ucc_key')
    code = sgqlc.types.Field(String, graphql_name='code')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_calibration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCalibration')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(Int, graphql_name='parentId')
    path_info = sgqlc.types.Field(sgqlc.types.non_null('ThingCategoryPathInfo'), graphql_name='pathInfo')
    ucc_field = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingCategoryUCCField'))), graphql_name='uccField')
    ucc_key = sgqlc.types.Field(String, graphql_name='uccKey')


class ThingCategoryList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingCategory))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingCategoryPathInfo(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('path_code', 'path_name', 'top_category_code', 'top_category_name')
    path_code = sgqlc.types.Field(String, graphql_name='pathCode')
    path_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pathName')
    top_category_code = sgqlc.types.Field(String, graphql_name='topCategoryCode')
    top_category_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='topCategoryName')


class ThingCategoryUCCField(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'id', 'key', 'name', 'thing_category_name')
    data = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='data')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_category_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='thingCategoryName')


class ThingCategoryUCCFieldList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingCategoryUCCField))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingChangeBorrowDraft(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'data', 'id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingChangeBorrowDraftData'))), graphql_name='data')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class ThingChangeBorrowDraftData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('change_return_at', 'thing', 'thing_circulation')
    change_return_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='changeReturnAt')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')
    thing_circulation = sgqlc.types.Field(sgqlc.types.non_null('ThingCirculation'), graphql_name='thingCirculation')


class ThingCirculation(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('borrow_at', 'borrow_remark', 'expected_borrow_at', 'expected_return_at', 'id', 'return_at', 'return_remark', 'state', 'thing', 'thing_borrow')
    borrow_at = sgqlc.types.Field(Timestamp, graphql_name='borrowAt')
    borrow_remark = sgqlc.types.Field(String, graphql_name='borrowRemark')
    expected_borrow_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='expectedBorrowAt')
    expected_return_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='expectedReturnAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    return_at = sgqlc.types.Field(Timestamp, graphql_name='returnAt')
    return_remark = sgqlc.types.Field(String, graphql_name='returnRemark')
    state = sgqlc.types.Field(sgqlc.types.non_null(BorrowState), graphql_name='state')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')
    thing_borrow = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrow), graphql_name='thingBorrow')


class ThingCirculationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingCirculation))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingCirculationOverview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('borrow_count', 'return_count', 'total_count')
    borrow_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='borrowCount')
    return_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='returnCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingCompleteFileRule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('attachment_field', 'id', 'thing_category')
    attachment_field = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EamField))), graphql_name='attachmentField')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    thing_category = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingCategory))), graphql_name='thingCategory')


class ThingCompleteFileRuleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingCompleteFileRule))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingFunctionDepartment(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default_calibrate_user', 'department', 'id')
    default_calibrate_user = sgqlc.types.Field('User', graphql_name='defaultCalibrateUser')
    department = sgqlc.types.Field(sgqlc.types.non_null(Department), graphql_name='department')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class ThingFunctionDepartmentList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingFunctionDepartment))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingGroup(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'id', 'is_selected', 'name', 'parent_id', 'path_name')
    code = sgqlc.types.Field(String, graphql_name='code')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_selected = sgqlc.types.Field(Boolean, graphql_name='isSelected')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')
    path_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pathName')


class ThingGroupList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingGroup)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInspection(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'create_by', 'create_method', 'created_at', 'estimated_time', 'id', 'operator', 'related_operator', 'status', 'thing_inspection_process_item', 'updated_at')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    create_by = sgqlc.types.Field('User', graphql_name='createBy')
    create_method = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionCreateType), graphql_name='createMethod')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    estimated_time = sgqlc.types.Field(String, graphql_name='estimatedTime')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    related_operator = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='relatedOperator')
    status = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionStatus), graphql_name='status')
    thing_inspection_process_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingInspectionProcessItem'))), graphql_name='thingInspectionProcessItem')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class ThingInspectionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingInspection))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInspectionOperatorRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(InspectionOperatorRecord)), graphql_name='data')


class ThingInspectionProcessItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('inspection_process_item', 'thing')
    inspection_process_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InspectionProcessItem))), graphql_name='inspectionProcessItem')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')


class ThingInspectionStatusOverview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('finished_count', 'inspecting_count', 'pending_count', 'total_count')
    finished_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='finishedCount')
    inspecting_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='inspectingCount')
    pending_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pendingCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInspectionWorkflowConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionStatus), graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionStatus), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionTrigger), graphql_name='trigger')


class ThingInspectionWorkflowConfigurationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingInspectionWorkflowConfiguration))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInventoryRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('created_by', 'id', 'image', 'label', 'remark', 'state', 'thing', 'updated_at')
    created_by = sgqlc.types.Field('User', graphql_name='createdBy')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EamFile)), graphql_name='image')
    label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInventoryLabel)), graphql_name='label')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    state = sgqlc.types.Field(sgqlc.types.non_null(ThingInventoryState), graphql_name='state')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class ThingInventoryRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingInventoryRecord))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInventoryRedundantRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('created_at', 'created_by', 'id', 'image', 'remark')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    created_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createdBy')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EamFile)), graphql_name='image')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class ThingInventoryRedundantRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingInventoryRedundantRecord))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInventoryRelateResourceList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('created_by',)
    created_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='createdBy')


class ThingInventoryThingFilter(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('department', 'thing_category')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Department)), graphql_name='department')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingCategory)), graphql_name='thingCategory')


class ThingInventoryTicket(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('constraint', 'count_summary', 'created_at', 'created_by', 'id', 'is_tracked', 'method', 'name', 'plan_at', 'remark', 'state', 'thing_filter', 'user_scope')
    constraint = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInventoryConstraint)), graphql_name='constraint')
    count_summary = sgqlc.types.Field(sgqlc.types.non_null('ThingInventoryTicketCountSummary'), graphql_name='countSummary')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    created_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createdBy')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_tracked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTracked')
    method = sgqlc.types.Field(sgqlc.types.non_null(ThingInventoryMethod), graphql_name='method')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    plan_at = sgqlc.types.Field(sgqlc.types.non_null(TimestampRange), graphql_name='planAt')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    state = sgqlc.types.Field(sgqlc.types.non_null(ThingInventoryTicketState), graphql_name='state')
    thing_filter = sgqlc.types.Field(ThingInventoryThingFilter, graphql_name='thingFilter')
    user_scope = sgqlc.types.Field(sgqlc.types.non_null(ThingInventoryUserScope), graphql_name='userScope')


class ThingInventoryTicketCountSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('finished_thing_count', 'lack_thing_count', 'redundant_thing_count', 'un_finished_thing_count')
    finished_thing_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='finishedThingCount')
    lack_thing_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='lackThingCount')
    redundant_thing_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='redundantThingCount')
    un_finished_thing_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='unFinishedThingCount')


class ThingInventoryTicketList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingInventoryTicket))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInventoryTrackRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'record')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    record = sgqlc.types.Field(sgqlc.types.non_null(ThingInventoryRecord), graphql_name='record')


class ThingInventoryTrackRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingInventoryTrackRecord))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInventoryTrackRedundantRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'record')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    record = sgqlc.types.Field(sgqlc.types.non_null(ThingInventoryRedundantRecord), graphql_name='record')


class ThingInventoryTrackRedundantRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingInventoryTrackRedundantRecord))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingIsLentOverview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('is_lent_count', 'not_lent_count', 'total_count')
    is_lent_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='isLentCount')
    not_lent_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='notLentCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingLabel(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class ThingLabelList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingLabel))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Thing))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingMaintenance(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'create_by', 'create_method', 'created_at', 'estimated_time', 'id', 'operator', 'related_operator', 'status', 'thing', 'thing_maintenance_process_item', 'updated_at')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    create_by = sgqlc.types.Field('User', graphql_name='createBy')
    create_method = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceCreateType), graphql_name='createMethod')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    estimated_time = sgqlc.types.Field(String, graphql_name='estimatedTime')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    related_operator = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='relatedOperator')
    status = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceStatus), graphql_name='status')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Thing))), graphql_name='thing')
    thing_maintenance_process_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingMaintenanceProcessItem'))), graphql_name='thingMaintenanceProcessItem')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class ThingMaintenanceList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingMaintenance))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingMaintenanceOperatorRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('apply_depository_name', 'apply_factory_name', 'apply_remark', 'apply_spare_part_names', 'cost_time', 'created_at', 'id', 'lack_depository_name', 'lack_factory_name', 'lack_spare_part_names', 'operator', 'operator_record_type', 'pause_reason', 'remark', 'restart_operator', 'turn_to')
    apply_depository_name = sgqlc.types.Field(String, graphql_name='applyDepositoryName')
    apply_factory_name = sgqlc.types.Field(String, graphql_name='applyFactoryName')
    apply_remark = sgqlc.types.Field(String, graphql_name='applyRemark')
    apply_spare_part_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='applySparePartNames')
    cost_time = sgqlc.types.Field(Int, graphql_name='costTime')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    lack_depository_name = sgqlc.types.Field(String, graphql_name='lackDepositoryName')
    lack_factory_name = sgqlc.types.Field(String, graphql_name='lackFactoryName')
    lack_spare_part_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lackSparePartNames')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    operator_record_type = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceOperatorType), graphql_name='operatorRecordType')
    pause_reason = sgqlc.types.Field(String, graphql_name='pauseReason')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    restart_operator = sgqlc.types.Field('User', graphql_name='restartOperator')
    turn_to = sgqlc.types.Field('User', graphql_name='turnTo')


class ThingMaintenanceOperatorRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ThingMaintenanceOperatorRecord)), graphql_name='data')


class ThingMaintenanceProcessItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('maintenance_process_item', 'maintenance_spare_part_item', 'thing')
    maintenance_process_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MaintenanceProcessItem))), graphql_name='maintenanceProcessItem')
    maintenance_spare_part_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MaintenanceSparePartItem))), graphql_name='maintenanceSparePartItem')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')


class ThingMaintenanceStatusOverview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('finished_count', 'maintaining_count', 'paused_count', 'pending_count', 'total_count', 'under_review_count')
    finished_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='finishedCount')
    maintaining_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maintainingCount')
    paused_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pausedCount')
    pending_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pendingCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    under_review_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='underReviewCount')


class ThingMaintenanceWorkflowConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceStatus), graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceStatus), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceTrigger), graphql_name='trigger')


class ThingMaintenanceWorkflowConfigurationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingMaintenanceWorkflowConfiguration))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingOnStateOverview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('abandoned_count', 'available_count', 'debugging_count', 'in_use_count', 'off_lease_count', 'other_count', 'pending_count', 'processed_count', 'repairing_count', 'stock_in_count', 'total_count')
    abandoned_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='AbandonedCount')
    available_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='AvailableCount')
    debugging_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='DebuggingCount')
    in_use_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='InUseCount')
    off_lease_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='OffLeaseCount')
    other_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='OtherCount')
    pending_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='PendingCount')
    processed_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ProcessedCount')
    repairing_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='RepairingCount')
    stock_in_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='StockInCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingRelateResourceList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('department', 'manager')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Department)), graphql_name='department')
    manager = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='manager')


class ThingRepair(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'create_by', 'created_at', 'estimated_time', 'found_at', 'id', 'operator', 'related_operator', 'status', 'thing', 'thing_repair_process_item', 'updated_at')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    create_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createBy')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    estimated_time = sgqlc.types.Field(String, graphql_name='estimatedTime')
    found_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='foundAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    related_operator = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='relatedOperator')
    status = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairStatus), graphql_name='status')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Thing))), graphql_name='thing')
    thing_repair_process_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingRepairProcessItem'))), graphql_name='thingRepairProcessItem')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class ThingRepairList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingRepair))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingRepairOperatorRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('apply_depository_name', 'apply_factory_name', 'apply_remark', 'apply_spare_part_names', 'cost_time', 'created_at', 'id', 'lack_depository_name', 'lack_factory_name', 'lack_spare_part_names', 'operator', 'operator_record_type', 'pause_reason', 'remark', 'restart_operator', 'turn_to')
    apply_depository_name = sgqlc.types.Field(String, graphql_name='applyDepositoryName')
    apply_factory_name = sgqlc.types.Field(String, graphql_name='applyFactoryName')
    apply_remark = sgqlc.types.Field(String, graphql_name='applyRemark')
    apply_spare_part_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='applySparePartNames')
    cost_time = sgqlc.types.Field(Int, graphql_name='costTime')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    lack_depository_name = sgqlc.types.Field(String, graphql_name='lackDepositoryName')
    lack_factory_name = sgqlc.types.Field(String, graphql_name='lackFactoryName')
    lack_spare_part_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lackSparePartNames')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    operator_record_type = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairOperatorType), graphql_name='operatorRecordType')
    pause_reason = sgqlc.types.Field(String, graphql_name='pauseReason')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    restart_operator = sgqlc.types.Field('User', graphql_name='restartOperator')
    turn_to = sgqlc.types.Field('User', graphql_name='turnTo')


class ThingRepairOperatorRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ThingRepairOperatorRecord)), graphql_name='data')


class ThingRepairProcessItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('after_repair_image', 'before_repair_image', 'id', 'remark', 'repair_content', 'repair_spare_part_item', 'repair_type', 'thing')
    after_repair_image = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EamFile))), graphql_name='afterRepairImage')
    before_repair_image = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EamFile))), graphql_name='beforeRepairImage')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    repair_content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repairContent')
    repair_spare_part_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RepairSparePartItem))), graphql_name='repairSparePartItem')
    repair_type = sgqlc.types.Field(ThingRepairType, graphql_name='repairType')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')


class ThingRepairStatusOverview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('finished_count', 'paused_count', 'pending_count', 'repairing_count', 'total_count', 'under_review_count')
    finished_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='finishedCount')
    paused_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pausedCount')
    pending_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pendingCount')
    repairing_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='repairingCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    under_review_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='underReviewCount')


class ThingRepairWorkflowConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairStatus), graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairStatus), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairTrigger), graphql_name='trigger')


class ThingRepairWorkflowConfigurationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingRepairWorkflowConfiguration))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingSchedule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('end_at', 'estimated_time', 'id', 'inspection_method', 'maintenance_method', 'name', 'operator', 'repeat', 'start_at', 'thing', 'ticket_type')
    end_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endAt')
    estimated_time = sgqlc.types.Field(String, graphql_name='estimatedTime')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    inspection_method = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InspectionMethod))), graphql_name='inspectionMethod')
    maintenance_method = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MaintenanceMethod))), graphql_name='maintenanceMethod')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    repeat = sgqlc.types.Field(sgqlc.types.non_null(Repeat), graphql_name='repeat')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Thing))), graphql_name='thing')
    ticket_type = sgqlc.types.Field(sgqlc.types.non_null(TicketType), graphql_name='ticketType')


class ThingScheduleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingSchedule))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingTask(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('execution_at', 'id', 'inspection_method', 'maintenance_method', 'operator', 'schedule', 'thing', 'thing_inspection', 'thing_maintenance')
    execution_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='executionAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    inspection_method = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InspectionMethod))), graphql_name='inspectionMethod')
    maintenance_method = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MaintenanceMethod))), graphql_name='maintenanceMethod')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    schedule = sgqlc.types.Field(sgqlc.types.non_null(ThingSchedule), graphql_name='schedule')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Thing))), graphql_name='thing')
    thing_inspection = sgqlc.types.Field(ThingInspection, graphql_name='thingInspection')
    thing_maintenance = sgqlc.types.Field(ThingMaintenance, graphql_name='thingMaintenance')


class ThingTaskList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingTask))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingTransferRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('apply_for_at', 'apply_for_user', 'expected_borrow_at', 'expected_return_at', 'field_data', 'group_file', 'id', 'opinion', 'process_id', 'sap_code_after_transfer', 'sap_code_before_transfer', 'transfer_in_department', 'transfer_out_department', 'transfer_type')
    apply_for_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='applyForAt')
    apply_for_user = sgqlc.types.Field('User', graphql_name='applyForUser')
    expected_borrow_at = sgqlc.types.Field(Timestamp, graphql_name='expectedBorrowAt')
    expected_return_at = sgqlc.types.Field(Timestamp, graphql_name='expectedReturnAt')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    group_file = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GroupFile))), graphql_name='groupFile')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    opinion = sgqlc.types.Field(String, graphql_name='opinion')
    process_id = sgqlc.types.Field(String, graphql_name='processId')
    sap_code_after_transfer = sgqlc.types.Field(String, graphql_name='sapCodeAfterTransfer')
    sap_code_before_transfer = sgqlc.types.Field(String, graphql_name='sapCodeBeforeTransfer')
    transfer_in_department = sgqlc.types.Field(Department, graphql_name='transferInDepartment')
    transfer_out_department = sgqlc.types.Field(Department, graphql_name='transferOutDepartment')
    transfer_type = sgqlc.types.Field(sgqlc.types.non_null(ThingTransferType), graphql_name='transferType')


class ThingTransferRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingTransferRecord))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingUCC(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'key', 'name', 'thing_category')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_category = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingCategory))), graphql_name='thingCategory')


class ThingUCCList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingUCC))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UCCField(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'meta', 'name', 'required', 'role', 'width')
    id = sgqlc.types.Field(String, graphql_name='id')
    meta = sgqlc.types.Field('UCCMeta', graphql_name='meta')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    required = sgqlc.types.Field(Boolean, graphql_name='required')
    role = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='role')
    width = sgqlc.types.Field(Int, graphql_name='width')


class UCCFormStructure(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'key', 'zone')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    zone = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of(UCCField)), graphql_name='zone')


class UCCMetaAttachment(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('attachment_type', 'extension', 'field_type', 'hint', 'id', 'max_count', 'max_size')
    attachment_type = sgqlc.types.Field(UCCAttachmentType, graphql_name='attachmentType')
    extension = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='extension')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    max_count = sgqlc.types.Field(Int, graphql_name='maxCount')
    max_size = sgqlc.types.Field(Int, graphql_name='maxSize')


class UCCMetaDate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default_bool', 'field_type', 'format', 'hint', 'id')
    default_bool = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='defaultBool')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    format = sgqlc.types.Field(String, graphql_name='format')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class UCCMetaLabel(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('content', 'field_type', 'id')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class UCCMetaMultiRadio(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default_str_list', 'field_type', 'id', 'option')
    default_str_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='defaultStrList')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    option = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='option')


class UCCMetaRadio(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default_str', 'field_type', 'id', 'option')
    default_str = sgqlc.types.Field(String, graphql_name='defaultStr')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    option = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='option')


class UCCMetaRange(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('field_type', 'id', 'max_range', 'min_range', 'round')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    max_range = sgqlc.types.Field(sgqlc.types.non_null('UCCMetaRangeExtremum'), graphql_name='maxRange')
    min_range = sgqlc.types.Field(sgqlc.types.non_null('UCCMetaRangeExtremum'), graphql_name='minRange')
    round = sgqlc.types.Field(Int, graphql_name='round')


class UCCMetaRangeExtremum(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default', 'field_type', 'hint', 'id', 'max', 'min', 'required', 'unit', 'zeroable')
    default = sgqlc.types.Field(Float, graphql_name='default')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    max = sgqlc.types.Field(Float, graphql_name='max')
    min = sgqlc.types.Field(Float, graphql_name='min')
    required = sgqlc.types.Field(Boolean, graphql_name='required')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    zeroable = sgqlc.types.Field(Boolean, graphql_name='zeroable')


class UCCMetaSelectBox(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default_str', 'default_str_list', 'field_type', 'hint', 'id', 'multi', 'option')
    default_str = sgqlc.types.Field(String, graphql_name='defaultStr')
    default_str_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='defaultStrList')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    multi = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='multi')
    option = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='option')


class UCCMetaSet(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('field_type', 'meta')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    meta = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UCCMeta')), graphql_name='meta')


class UCCMetaText(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default_num', 'default_str', 'field_type', 'hint', 'id', 'label', 'max', 'min', 'round', 'type', 'unit', 'zeroable')
    default_num = sgqlc.types.Field(Float, graphql_name='defaultNum')
    default_str = sgqlc.types.Field(String, graphql_name='defaultStr')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    label = sgqlc.types.Field(String, graphql_name='label')
    max = sgqlc.types.Field(Float, graphql_name='max')
    min = sgqlc.types.Field(Float, graphql_name='min')
    round = sgqlc.types.Field(Int, graphql_name='round')
    type = sgqlc.types.Field(sgqlc.types.non_null(UCCFiledValue), graphql_name='type')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    zeroable = sgqlc.types.Field(Boolean, graphql_name='zeroable')


class UploadConfig(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name', 'url')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class User(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('account', 'all_authorizations', 'avatar', 'created_at', 'email', 'id', 'is_admin', 'is_allowed_to_login', 'is_email_verified', 'is_phone_number_verified', 'name', 'organizations', 'phone_number', 'remark', 'roles', 'tenant', 'thing_group', 'updated_at')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    all_authorizations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Authorization))), graphql_name='allAuthorizations')
    avatar = sgqlc.types.Field(Image, graphql_name='avatar')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    is_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAdmin')
    is_allowed_to_login = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAllowedToLogin')
    is_email_verified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEmailVerified')
    is_phone_number_verified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPhoneNumberVerified')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    organizations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Organization))), graphql_name='organizations')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    roles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Role))), graphql_name='roles')
    tenant = sgqlc.types.Field(sgqlc.types.non_null(Tenant), graphql_name='tenant')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingGroup))), graphql_name='thingGroup')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class UserAuthorizationRule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('authorization_rule_id', 'id', 'user_id')
    authorization_rule_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='authorization_rule_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='user_id')


class UserBacklog(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('backlog_id', 'id', 'user_id')
    backlog_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='backlogId')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')


class UserList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(User))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserStaredApp(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app_id', 'id', 'user_id')
    app_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='appId')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')


class UserStaredPage(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'page_id', 'rank', 'user_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    page_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pageId')
    rank = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rank')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')


class UserThingGroupList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UserThingGroups')), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserThingGroups(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('thing_groups', 'user')
    thing_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingGroup)), graphql_name='thingGroups')
    user = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='user')


class WecomUser(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name', 'open_userid')
    name = sgqlc.types.Field(String, graphql_name='name')
    open_userid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='openUserid')


class WorkbenchCard(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class WorkflowBaseConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('change_borrow_init_state', 'change_borrow_use_default_workflow', 'thing_borrow_init_state', 'thing_borrow_use_default_workflow', 'thing_calibrate_init_state', 'thing_calibrate_use_default_workflow', 'thing_inspection_init_state', 'thing_inspection_use_default_workflow', 'thing_maintenance_init_state', 'thing_maintenance_use_default_workflow', 'thing_repair_init_state', 'thing_repair_use_default_workflow')
    change_borrow_init_state = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowState), graphql_name='changeBorrowInitState')
    change_borrow_use_default_workflow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='changeBorrowUseDefaultWorkflow')
    thing_borrow_init_state = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowState), graphql_name='thingBorrowInitState')
    thing_borrow_use_default_workflow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='thingBorrowUseDefaultWorkflow')
    thing_calibrate_init_state = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateState), graphql_name='thingCalibrateInitState')
    thing_calibrate_use_default_workflow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='thingCalibrateUseDefaultWorkflow')
    thing_inspection_init_state = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionStatus), graphql_name='thingInspectionInitState')
    thing_inspection_use_default_workflow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='thingInspectionUseDefaultWorkflow')
    thing_maintenance_init_state = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceStatus), graphql_name='thingMaintenanceInitState')
    thing_maintenance_use_default_workflow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='thingMaintenanceUseDefaultWorkflow')
    thing_repair_init_state = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairStatus), graphql_name='thingRepairInitState')
    thing_repair_use_default_workflow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='thingRepairUseDefaultWorkflow')


class WorkflowDefaultInitState(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('change_borrow_default_init_state', 'thing_borrow_default_init_state', 'thing_calibrate_init_default_state', 'thing_inspection_default_init_state', 'thing_maintenance_default_init_state', 'thing_repair_init_default_state')
    change_borrow_default_init_state = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowState), graphql_name='changeBorrowDefaultInitState')
    thing_borrow_default_init_state = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowState), graphql_name='thingBorrowDefaultInitState')
    thing_calibrate_init_default_state = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateState), graphql_name='thingCalibrateInitDefaultState')
    thing_inspection_default_init_state = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionStatus), graphql_name='thingInspectionDefaultInitState')
    thing_maintenance_default_init_state = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceStatus), graphql_name='thingMaintenanceDefaultInitState')
    thing_repair_init_default_state = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairStatus), graphql_name='thingRepairInitDefaultState')


class AuthenticationSourceLDAP3(sgqlc.types.Type, AuthenticationSource):
    __schema__ = platform_schema
    __field_names__ = ('bind_dn', 'bind_password', 'email_attribute', 'encryption_method', 'host', 'name_attribute', 'phone_attribute', 'port', 'uid_attribute', 'user_search_base_dn', 'user_search_filter')
    bind_dn = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bindDN')
    bind_password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bindPassword')
    email_attribute = sgqlc.types.Field(String, graphql_name='emailAttribute')
    encryption_method = sgqlc.types.Field(sgqlc.types.non_null(LDAP3EncryptionMethod), graphql_name='encryptionMethod')
    host = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='host')
    name_attribute = sgqlc.types.Field(String, graphql_name='nameAttribute')
    phone_attribute = sgqlc.types.Field(String, graphql_name='phoneAttribute')
    port = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='port')
    uid_attribute = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uidAttribute')
    user_search_base_dn = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userSearchBaseDN')
    user_search_filter = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userSearchFilter')


class AuthenticationSourceOAuth2(sgqlc.types.Type, AuthenticationSource):
    __schema__ = platform_schema
    __field_names__ = ('authorization_url', 'client_id', 'client_secret', 'email_attribute', 'name_attribute', 'phone_attribute', 'scope', 'token_url', 'uid_attribute', 'user_info_url')
    authorization_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='authorizationURL')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientID')
    client_secret = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientSecret')
    email_attribute = sgqlc.types.Field(String, graphql_name='emailAttribute')
    name_attribute = sgqlc.types.Field(String, graphql_name='nameAttribute')
    phone_attribute = sgqlc.types.Field(String, graphql_name='phoneAttribute')
    scope = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='scope')
    token_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenURL')
    uid_attribute = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uidAttribute')
    user_info_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userInfoURL')


class AuthenticationSourceOpenIDConnect1(sgqlc.types.Type, AuthenticationSource):
    __schema__ = platform_schema
    __field_names__ = ('authorization_url', 'client_id', 'client_secret', 'configuration_method', 'configuration_url', 'email_attribute', 'jwks_url', 'name_attribute', 'phone_attribute', 'scope', 'token_url', 'uid_attribute')
    authorization_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='authorizationURL')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientID')
    client_secret = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientSecret')
    configuration_method = sgqlc.types.Field(sgqlc.types.non_null(OpenIDConnect1ConfigurationMethod), graphql_name='configurationMethod')
    configuration_url = sgqlc.types.Field(String, graphql_name='configurationURL')
    email_attribute = sgqlc.types.Field(String, graphql_name='emailAttribute')
    jwks_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='jwksURL')
    name_attribute = sgqlc.types.Field(String, graphql_name='nameAttribute')
    phone_attribute = sgqlc.types.Field(String, graphql_name='phoneAttribute')
    scope = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='scope')
    token_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenURL')
    uid_attribute = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uidAttribute')


class AuthenticationSourceSAML2(sgqlc.types.Type, AuthenticationSource):
    __schema__ = platform_schema
    __field_names__ = ()


class OAuth2AuthenticationConfiguration(sgqlc.types.Type, AuthenticationConfiguration):
    __schema__ = platform_schema
    __field_names__ = ('access_token_attribute_path', 'account_attribute_path', 'authorization_url', 'client_authentication_method', 'client_id', 'client_secret', 'do_update_local_user_info_when_login', 'email_attribute_path', 'name_attribute_path', 'phone_number_attribute_path', 'scope', 'support_state', 'token_response_format', 'token_url', 'user_info_authentication_method', 'user_info_request_method', 'user_info_response_format', 'user_info_url')
    access_token_attribute_path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accessTokenAttributePath')
    account_attribute_path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accountAttributePath')
    authorization_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='authorizationUrl')
    client_authentication_method = sgqlc.types.Field(sgqlc.types.non_null(AuthenticationMethod), graphql_name='clientAuthenticationMethod')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')
    client_secret = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientSecret')
    do_update_local_user_info_when_login = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='doUpdateLocalUserInfoWhenLogin')
    email_attribute_path = sgqlc.types.Field(String, graphql_name='emailAttributePath')
    name_attribute_path = sgqlc.types.Field(String, graphql_name='nameAttributePath')
    phone_number_attribute_path = sgqlc.types.Field(String, graphql_name='phoneNumberAttributePath')
    scope = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='scope')
    support_state = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='supportState')
    token_response_format = sgqlc.types.Field(sgqlc.types.non_null(ResponseFormat), graphql_name='tokenResponseFormat')
    token_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenUrl')
    user_info_authentication_method = sgqlc.types.Field(sgqlc.types.non_null(AuthenticationMethod), graphql_name='userInfoAuthenticationMethod')
    user_info_request_method = sgqlc.types.Field(sgqlc.types.non_null(UserInfoRequestMethod), graphql_name='userInfoRequestMethod')
    user_info_response_format = sgqlc.types.Field(sgqlc.types.non_null(ResponseFormat), graphql_name='userInfoResponseFormat')
    user_info_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userInfoUrl')


class OAuth2LoginConfiguration(sgqlc.types.Type, LoginConfiguration):
    __schema__ = platform_schema
    __field_names__ = ('authentication_configuration_name', 'login_url')
    authentication_configuration_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='authenticationConfigurationName')
    login_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='loginUrl')


class OpenIDConnect1AuthenticationConfiguration(sgqlc.types.Type, AuthenticationConfiguration):
    __schema__ = platform_schema
    __field_names__ = ('account_attribute_path', 'client_id', 'client_secret', 'configuration_url', 'do_update_local_user_info_when_login', 'email_attribute_path', 'name_attribute_path', 'phone_number_attribute_path', 'scope')
    account_attribute_path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accountAttributePath')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')
    client_secret = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientSecret')
    configuration_url = sgqlc.types.Field(String, graphql_name='configurationUrl')
    do_update_local_user_info_when_login = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='doUpdateLocalUserInfoWhenLogin')
    email_attribute_path = sgqlc.types.Field(String, graphql_name='emailAttributePath')
    name_attribute_path = sgqlc.types.Field(String, graphql_name='nameAttributePath')
    phone_number_attribute_path = sgqlc.types.Field(String, graphql_name='phoneNumberAttributePath')
    scope = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='scope')


class OpenIDConnect1LoginConfiguration(sgqlc.types.Type, LoginConfiguration):
    __schema__ = platform_schema
    __field_names__ = ('authentication_configuration_name', 'login_url')
    authentication_configuration_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='authenticationConfigurationName')
    login_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='loginUrl')


class SystemLoginConfiguration(sgqlc.types.Type, LoginConfiguration):
    __schema__ = platform_schema
    __field_names__ = ('tenant_code',)
    tenant_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tenantCode')



########################################################################
# Unions
########################################################################
class EamMeta(sgqlc.types.Union):
    __schema__ = platform_schema
    __types__ = (EamMetaAttachment, EamMetaDate, EamMetaLabel, EamMetaMultiRadio, EamMetaNumber, EamMetaOther, EamMetaRadio, EamMetaRange, EamMetaSelectBox, EamMetaSet, EamMetaText)


class UCCMeta(sgqlc.types.Union):
    __schema__ = platform_schema
    __types__ = (UCCMetaAttachment, UCCMetaDate, UCCMetaLabel, UCCMetaMultiRadio, UCCMetaRadio, UCCMetaRange, UCCMetaSelectBox, UCCMetaSet, UCCMetaText)



########################################################################
# Schema Entry Points
########################################################################
platform_schema.query_type = Query
platform_schema.mutation_type = Mutation
platform_schema.subscription_type = None

