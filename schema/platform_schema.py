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


Boolean = sgqlc.types.Boolean

class ChannelStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('AVAILABLE', 'UNAVAILABLE')


class DifferenceResult(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ADDED', 'REMOVED')


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


class MessageChannelKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('EMAIL', 'INBOX', 'WECOM')


class MessageKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FILE', 'IMAGE', 'TEXT', 'TEXT_CARD', 'VIDEO')


class OpenIDConnect1ConfigurationMethod(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DISCOVERY', 'MANUAL')


class PermissionType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FEATURE', 'MENU', 'PAGE')


class PushScheduleType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CRON', 'IMMEDIATELY')


class ResponseFormat(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FORM', 'JSON')


String = sgqlc.types.String

class TableFieldGroup(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CUSTOM', 'FIXED', 'SCROLLABLE')


class TemplateStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DISABLED', 'ENABLED')


class TenantStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DISABLED', 'ENABLED')


class TenantType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('COMPANY', 'PLATFORM')


class Timestamp(sgqlc.types.Scalar):
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


class AuthorizationRuleFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('is_leaf_only', 'permission_types')
    is_leaf_only = sgqlc.types.Field(Boolean, graphql_name='isLeafOnly')
    permission_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PermissionType)), graphql_name='permissionTypes')


class BIFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('aggregation', 'end', 'granularity', 'metric', 'series', 'start')
    aggregation = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='aggregation')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    granularity = sgqlc.types.Field(Granularity, graphql_name='granularity')
    metric = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='metric')
    series = sgqlc.types.Field(String, graphql_name='series')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')


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


class CityFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('province',)
    province = sgqlc.types.Field('StringIDInput', graphql_name='province')


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


class CreateAppVersionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app_id', 'description', 'version')
    app_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='appId')
    description = sgqlc.types.Field(String, graphql_name='description')
    version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='version')


class CreateCompanyBIDatasourceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'datasource')
    company = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='company')
    datasource = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='datasource')


class CreateEnterpriseAppInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('description', 'name')
    description = sgqlc.types.Field(String, graphql_name='description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


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


class CreateRoleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('description', 'name')
    description = sgqlc.types.Field(String, graphql_name='description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


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


class DepartmentListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company', 'current_only', 'ids', 'search')
    code = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='code')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    current_only = sgqlc.types.Field(Boolean, graphql_name='currentOnly')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='ids')
    search = sgqlc.types.Field(String, graphql_name='search')


class DepartmentTreeFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company',)
    company = sgqlc.types.Field('IDInput', graphql_name='company')


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


class FieldInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'description', 'example', 'is_target', 'name')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    description = sgqlc.types.Field(String, graphql_name='description')
    example = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='example')
    is_target = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTarget')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IDInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class InboxMessageFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('is_read', 'source_app_keys')
    is_read = sgqlc.types.Field(Boolean, graphql_name='isRead')
    source_app_keys = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sourceAppKeys')


class IntIDInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


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


class LoginInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account', 'password', 'tenant_code')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    tenant_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tenantCode')


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


class OldRoleFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'permission', 'scope', 'search')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    id = sgqlc.types.Field(ID, graphql_name='id')
    permission = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='permission')
    scope = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='scope')
    search = sgqlc.types.Field(String, graphql_name='search')


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


class PermissionDataRangeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'name')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class PermissionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids', 'types')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ids')
    types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PermissionType)), graphql_name='types')


class PushScheduleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('type',)
    type = sgqlc.types.Field(PushScheduleType, graphql_name='type')


class RenderStyleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('config', 'kind', 'meta_channel_id')
    config = sgqlc.types.Field(JSON, graphql_name='config')
    kind = sgqlc.types.Field(MessageKind, graphql_name='kind')
    meta_channel_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='meta_channel_id')


class RoleFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


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


class SetPermissionToTenantInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('permissions', 'tenant')
    permissions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput'))), graphql_name='permissions')
    tenant = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='tenant')


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


class StarAppInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app',)
    app = sgqlc.types.Field(sgqlc.types.non_null('StringIDInput'), graphql_name='app')


class StringIDInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')


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
    __field_names__ = ('city_ids', 'county_ids', 'industry_ids', 'province_ids', 'search')
    city_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='cityIds')
    county_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='countyIds')
    industry_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='industryIds')
    province_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='provinceIds')
    search = sgqlc.types.Field(String, graphql_name='search')


class TenantIndustryTreeNodeFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


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


class UpdateRoleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('description', 'id', 'name')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateTenantInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('address', 'city', 'code', 'county', 'email', 'id', 'industry', 'name', 'phone', 'province', 'uscc')
    address = sgqlc.types.Field(String, graphql_name='address')
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
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='ids')


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
    __field_names__ = ('data_ranges', 'is_allowed', 'permission_id')
    data_ranges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='dataRanges')
    is_allowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAllowed')
    permission_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='permissionId')


class AuthorizationRule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data_range', 'id', 'is_allowed', 'permission')
    data_range = sgqlc.types.Field('PermissionDataRange', graphql_name='dataRange')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    is_allowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAllowed')
    permission = sgqlc.types.Field(sgqlc.types.non_null('Permission'), graphql_name='permission')


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


class City(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('counties', 'id', 'name')
    counties = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('County')), graphql_name='counties')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


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
    __field_names__ = ('companies', 'id', 'name')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Company)), graphql_name='companies')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreatedUserInfo(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('password', 'user_id')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')


class Department(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'id', 'is_deleted', 'level', 'manager', 'name', 'parent_id', 'path_name')
    code = sgqlc.types.Field(String, graphql_name='code')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_deleted = sgqlc.types.Field(Boolean, graphql_name='isDeleted')
    level = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='level')
    manager = sgqlc.types.Field('User', graphql_name='manager')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentID')
    path_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pathName')


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


class LoginConfiguration(sgqlc.types.Interface):
    __schema__ = platform_schema
    __field_names__ = ('kind',)
    kind = sgqlc.types.Field(sgqlc.types.non_null(LoginConfigurationKind), graphql_name='kind')


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
    __field_names__ = ('_dummy', 'active_message_channel', 'add_meta_templates_to_tenant', 'assign_app_permissions', 'assign_tenant_apps', 'bind_my_email', 'change_my_password', 'change_my_password_by_email_verification', 'change_my_password_by_verify_code', 'company_login', 'configure_authentication_source_ldap3', 'configure_authentication_source_oauth2', 'configure_authentication_source_open_idconnect1', 'configure_authentication_source_saml2', 'create_app_version', 'create_company_bidatasource', 'create_enterprise_app', 'create_file', 'create_files', 'create_image', 'create_images', 'create_market_file', 'create_market_files', 'create_meta_template', 'create_oauth2_authentication_configuration', 'create_open_idconnect1_authentication_configuration', 'create_organization', 'create_role', 'create_tenant', 'create_tenant_owner', 'create_user', 'deactivate_message_channel', 'delete_app_version', 'delete_authentication_configuration', 'delete_company_bidatasource', 'delete_enterprise_apps', 'delete_message_templates_of_tenant', 'delete_meta_template', 'delete_organization', 'delete_role', 'delete_table_fields_config', 'delete_tenant', 'delete_users', 'disable_tenant', 'disable_users', 'duplicate_uccform_structure', 'enable_tenant', 'enable_users', 'login', 'login_by_email', 'logout', 'offline_app_version', 'online_app_version', 'overwrite_message_template', 'read_all_inbox_messages', 'read_inbox_messages', 'remove_authorization_rules_of_user', 'reset_app_client_secret', 'reset_authentication_source', 'reset_tenant_owner_password', 'reset_user_password', 'send_identity_verify_code_to_email', 'set_admin_users', 'set_authorization_rules_to_role', 'set_authorization_rules_to_user', 'set_channel_of_message_templates', 'set_channels_of_message_template', 'set_permissions_to_tenant', 'set_table_column_setting', 'set_table_fields_config', 'set_table_fixed_fields_config', 'set_uccform_structure', 'set_uccstack_data', 'set_workbench', 'star_app', 'transfer_tenant_owner', 'un_assign_app_permissions', 'un_assign_tenant_apps', 'un_star_app', 'unbind_email_of_users', 'unbind_my_email', 'unset_admin_users', 'update_app_version', 'update_authorization_rules_of_user', 'update_enterprise_app', 'update_me', 'update_meta_channel', 'update_meta_template', 'update_oauth2_authentication_configuration', 'update_open_idconnect1_authentication_configuration', 'update_organization', 'update_role', 'update_status_of_template', 'update_tenant', 'update_user', 'visit_app', 'visit_menu')
    _dummy = sgqlc.types.Field(Boolean, graphql_name='_dummy')
    active_message_channel = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='activeMessageChannel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    add_meta_templates_to_tenant = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addMetaTemplatesToTenant', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ids', default=None)),
        ('tenant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tenantId', default=None)),
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
    create_app_version = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createAppVersion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateAppVersionInput), graphql_name='input', default=None)),
))
    )
    create_company_bidatasource = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createCompanyBIDatasource', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCompanyBIDatasourceInput), graphql_name='input', default=None)),
))
    )
    create_enterprise_app = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createEnterpriseApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEnterpriseAppInput), graphql_name='input', default=None)),
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
    create_role = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateRoleInput), graphql_name='input', default=None)),
))
    )
    create_tenant = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createTenant', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateTenantInput), graphql_name='input', default=None)),
))
    )
    create_tenant_owner = sgqlc.types.Field(sgqlc.types.non_null(CreatedUserInfo), graphql_name='createTenantOwner', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateTenantOwnerInput), graphql_name='input', default=None)),
))
    )
    create_user = sgqlc.types.Field(sgqlc.types.non_null(CreatedUserInfo), graphql_name='createUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateUserInput), graphql_name='input', default=None)),
))
    )
    deactivate_message_channel = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deactivateMessageChannel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
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
    delete_company_bidatasource = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCompanyBIDatasource', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    delete_enterprise_apps = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteEnterpriseApps', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
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
    delete_role = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteRole', args=sgqlc.types.ArgDict((
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
    delete_users = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteUsers', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    disable_tenant = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='disableTenant', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    disable_users = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='disableUsers', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
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
    enable_users = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enableUsers', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
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
    logout = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='logout')
    offline_app_version = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='offlineAppVersion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    online_app_version = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='onlineAppVersion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    overwrite_message_template = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='overwriteMessageTemplate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
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
    remove_authorization_rules_of_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='removeAuthorizationRulesOfUser', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='ids', default=None)),
        ('user_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='userId', default=None)),
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
    reset_user_password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='resetUserPassword', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    send_identity_verify_code_to_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='sendIdentityVerifyCodeToEmail', args=sgqlc.types.ArgDict((
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
))
    )
    set_admin_users = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setAdminUsers', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    set_authorization_rules_to_role = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setAuthorizationRulesToRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetAuthorizationRulesToRoleInput), graphql_name='input', default=None)),
))
    )
    set_authorization_rules_to_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setAuthorizationRulesToUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetAuthorizationRulesToUserInput), graphql_name='input', default=None)),
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
    set_permissions_to_tenant = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setPermissionsToTenant', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetPermissionToTenantInput), graphql_name='input', default=None)),
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
    set_uccform_structure = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='setUCCFormStructure', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(SetUCCFormStructureInput, graphql_name='input', default=None)),
))
    )
    set_uccstack_data = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setUCCStackData', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetUCCStackDataInput), graphql_name='input', default=None)),
))
    )
    set_workbench = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setWorkbench', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='input', default=None)),
))
    )
    star_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='starApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(StarAppInput), graphql_name='input', default=None)),
))
    )
    transfer_tenant_owner = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='transferTenantOwner', args=sgqlc.types.ArgDict((
        ('target_user_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='targetUserId', default=None)),
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
    unbind_email_of_users = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unbindEmailOfUsers', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    unbind_my_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unbindMyEmail', args=sgqlc.types.ArgDict((
        ('verify_code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='verifyCode', default=None)),
))
    )
    unset_admin_users = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unsetAdminUsers', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    update_app_version = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateAppVersion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateAppVersionInput), graphql_name='input', default=None)),
))
    )
    update_authorization_rules_of_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateAuthorizationRulesOfUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateAuthorizationRulesOfUserInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateEnterpriseApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseAppInput), graphql_name='input', default=None)),
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
    update_role = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateRoleInput), graphql_name='input', default=None)),
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
    update_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserInput), graphql_name='input', default=None)),
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
    __field_names__ = ('log_list', 'admin_user_list', 'all_authorization_rules_of_role', 'all_permissions_of_user', 'apis', 'app_groups', 'app_menu_list', 'app_version_list', 'assignable_managers_of_organization', 'assignable_meta_template_list_of_tenant', 'assignable_permissions_of_tenant', 'assigned_permissions_of_app', 'authentication_configuration', 'authentication_source', 'authorization_rule_and_dependencies', 'authorization_rule_dependent_by', 'bi_issue_issue', 'children_of_department', 'cities', 'city_companies', 'companies', 'company_bidatasource_list', 'company_bidatasource_tree', 'counties', 'countries', 'department_by_id_and_level', 'department_list', 'department_tree', 'direct_authorization_rules_of_user', 'inbox_message', 'inbox_message_list', 'is_create_app_version_allowed', 'is_email_exists', 'is_email_verified', 'is_permission_changed_of_latest_app_version', 'login_configuration', 'managed_organizations_of_user', 'me', 'menu_visit_history_list', 'message_channels_of_tenant', 'message_template_list_of_tenant', 'meta_channels', 'meta_template', 'meta_template_event_exists', 'meta_template_list', 'my_app_list', 'my_tenant', 'my_tenant_app_list', 'my_tenant_development_app_list', 'organization', 'organization_by_code', 'organization_by_id_and_level', 'organization_code_exists', 'organization_list', 'organization_name_exists_in_siblings', 'organization_tree_nodes', 'permissions', 'permissions_of_tenant', 'provinces', 'recent_app', 'role', 'role_list', 'role_name_exists', 'root_organization', 'stared_apps', 'system_log_action', 'system_log_list', 'table_column_setting', 'table_fields_config', 'table_fixed_fields_config', 'tenant', 'tenant_app_list', 'tenant_code_exists', 'tenant_industry_tree_nodes', 'tenant_list', 'tenant_name_exists', 'tenant_uscc_exists', 'ucc_form_structure', 'ucc_form_structure_json_schema', 'ucc_stack_data', 'unread_message_apps', 'upload_config', 'upload_configs', 'user', 'user_account_exists', 'user_list', 'workbench', 'workbench_card_data', 'workbench_card_option')
    log_list = sgqlc.types.Field(sgqlc.types.non_null('LogList'), graphql_name='LogList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(LogListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    admin_user_list = sgqlc.types.Field(sgqlc.types.non_null('UserList'), graphql_name='adminUserList', args=sgqlc.types.ArgDict((
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
    all_permissions_of_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Permission))), graphql_name='allPermissionsOfUser', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(PermissionFilterInput, graphql_name='filter', default=None)),
        ('user_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='userId', default=None)),
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
    app_version_list = sgqlc.types.Field(sgqlc.types.non_null(AppVersionList), graphql_name='appVersionList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AppVersionListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    assignable_managers_of_organization = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='assignableManagersOfOrganization', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='organizationId', default=None)),
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
    authorization_rule_dependent_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AuthorizationRule))), graphql_name='authorizationRuleDependentBy', args=sgqlc.types.ArgDict((
        ('rule_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='ruleId', default=None)),
))
    )
    bi_issue_issue = sgqlc.types.Field(sgqlc.types.list_of(BIResult), graphql_name='biIssueIssue', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    children_of_department = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Department))), graphql_name='childrenOfDepartment', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='companyId', default=None)),
        ('department_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='departmentId', default=None)),
))
    )
    cities = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(City)), graphql_name='cities', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(CityFilterInput), graphql_name='filter', default=None)),
))
    )
    city_companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(City)), graphql_name='cityCompanies')
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
    counties = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(County)), graphql_name='counties', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(CountyFilterInput), graphql_name='filter', default=None)),
))
    )
    countries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Country)), graphql_name='countries', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(countryFilter, graphql_name='filter', default=None)),
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
    department_tree = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='departmentTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(DepartmentTreeFilter, graphql_name='filter', default=None)),
))
    )
    direct_authorization_rules_of_user = sgqlc.types.Field(sgqlc.types.non_null(AuthorizationRuleList), graphql_name='directAuthorizationRulesOfUser', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AuthorizationRuleFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('user_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='userId', default=None)),
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
    is_create_app_version_allowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCreateAppVersionAllowed', args=sgqlc.types.ArgDict((
        ('app_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='appId', default=None)),
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
    is_permission_changed_of_latest_app_version = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPermissionChangedOfLatestAppVersion', args=sgqlc.types.ArgDict((
        ('app_id', sgqlc.types.Arg(String, graphql_name='appId', default=None)),
))
    )
    login_configuration = sgqlc.types.Field(sgqlc.types.non_null(LoginConfiguration), graphql_name='loginConfiguration', args=sgqlc.types.ArgDict((
        ('tenant_code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tenantCode', default=None)),
))
    )
    managed_organizations_of_user = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Organization)), graphql_name='managedOrganizationsOfUser', args=sgqlc.types.ArgDict((
        ('user_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='userId', default=None)),
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
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Permission)), graphql_name='permissions', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(PermissionFilterInput, graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
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
    root_organization = sgqlc.types.Field(sgqlc.types.non_null(Organization), graphql_name='rootOrganization')
    stared_apps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(App))), graphql_name='staredApps')
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
    user = sgqlc.types.Field('User', graphql_name='user', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
))
    )
    user_account_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='userAccountExists', args=sgqlc.types.ArgDict((
        ('account', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='account', default=None)),
        ('tenant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tenantId', default=None)),
))
    )
    user_list = sgqlc.types.Field(sgqlc.types.non_null('UserList'), graphql_name='userList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(UserFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    workbench = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkbenchCard'))), graphql_name='workbench')
    workbench_card_data = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='workbenchCardData', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    workbench_card_option = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkbenchCard'))), graphql_name='workbenchCardOption')


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


class RoleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Role))), graphql_name='data')
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


class Tenant(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('address', 'city', 'code', 'company_id', 'county', 'created_at', 'email', 'id', 'industry', 'name', 'owner', 'phone', 'province', 'status', 'type', 'uscc')
    address = sgqlc.types.Field(String, graphql_name='address')
    city = sgqlc.types.Field(sgqlc.types.non_null(City), graphql_name='city')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='companyId')
    county = sgqlc.types.Field(sgqlc.types.non_null(County), graphql_name='county')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    industry = sgqlc.types.Field(sgqlc.types.non_null('TenantIndustry'), graphql_name='industry')
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
    __field_names__ = ('account', 'all_authorizations', 'avatar', 'created_at', 'email', 'email_is_verified', 'id', 'is_account_enabled', 'is_admin', 'is_user_enabled', 'name', 'organizations', 'phone_number', 'remark', 'roles', 'tenant', 'updated_at')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    all_authorizations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Authorization))), graphql_name='allAuthorizations')
    avatar = sgqlc.types.Field(Image, graphql_name='avatar')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    email = sgqlc.types.Field(String, graphql_name='email')
    email_is_verified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='emailIsVerified')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    is_account_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAccountEnabled')
    is_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAdmin')
    is_user_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isUserEnabled')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    organizations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Organization))), graphql_name='organizations')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    roles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Role))), graphql_name='roles')
    tenant = sgqlc.types.Field(sgqlc.types.non_null(Tenant), graphql_name='tenant')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


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


class WorkbenchCard(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


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
    __field_names__ = ()



########################################################################
# Unions
########################################################################
class UCCMeta(sgqlc.types.Union):
    __schema__ = platform_schema
    __types__ = (UCCMetaAttachment, UCCMetaDate, UCCMetaLabel, UCCMetaMultiRadio, UCCMetaRadio, UCCMetaRange, UCCMetaSelectBox, UCCMetaSet, UCCMetaText)



########################################################################
# Schema Entry Points
########################################################################
platform_schema.query_type = Query
platform_schema.mutation_type = Mutation
platform_schema.subscription_type = None

