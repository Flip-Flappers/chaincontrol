-- 文件名称: alert_config.sql
-- 文件描述: 此SQL文件用于创建用于存储告警配置的表 alert_config。
--         表中记录了告警配置信息，包括告警标识、创建与更新时间、启用状态、告警严重度、
--         关联消息模板、关联规则引擎、租户信息等，便于系统后续对告警的管理和处理。
-- 使用场景: 适用于需要对系统中各类告警进行配置管理、查询和维护的场景。
-- tag: 报警配置

CREATE TABLE alert_config
(
    id                  BIGINT       NOT NULL COMMENT '告警配置id，主键，用于唯一标识每个告警配置',
    create_by           BIGINT       NULL COMMENT '创建者，记录创建该记录的用户ID',
    create_dept         BIGINT       NULL COMMENT '创建部门，记录创建该记录的部门ID',
    create_time         DATETIME     NULL COMMENT '创建时间，记录记录创建的时间',
    update_by           BIGINT       NULL COMMENT '更新者，记录最后一次更新该记录的用户ID',
    update_time         DATETIME     NULL COMMENT '更新时间，记录最后一次更新的时间',
    create_at           BIGINT       NULL COMMENT '创建时间戳，可能用于记录精确的创建时间（与create_time含义可能重叠）',
    description         VARCHAR(255) NULL COMMENT '描述，对告警配置的详细说明',
    enable              BIT          NULL COMMENT '是否启用，标识告警配置当前的启用状态（如1：启用，0：禁用）',
    level               VARCHAR(255) NULL COMMENT '告警严重度，表示告警的严重级别（例如：低、中、高）',
    message_template_id VARCHAR(255) NULL COMMENT '关联消息转发模板ID，用于指定转发告警信息的消息模板',
    name                VARCHAR(255) NULL COMMENT '告警名称，用于识别和展示告警配置',
    rule_info_id        VARCHAR(255) NULL COMMENT '关联规则引擎ID，用于关联执行告警判断的规则引擎',
    tenant_id           BIGINT       NULL COMMENT '租户ID，用于多租户系统中标识所属租户',
    uid                 VARCHAR(255) NULL COMMENT '配置所属用户，标识该告警配置具体归属于哪个用户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='存储系统中各类告警配置的详细信息';


-- 文件名称: alert_record.sql
-- 文件描述: 此SQL文件用于创建存储告警记录的表 alert_record。
--         表中记录了告警的详细信息，包括告警记录标识、创建时间、告警触发时间、
--         告警详情、严重度等级、是否已读状态等，便于系统对告警记录进行存储、查询和历史追踪。
-- 使用场景: 当系统触发告警时，生成对应的告警记录并存入此表，支持后续的告警信息统计和用户通知。
-- tag: 报警纪录

CREATE TABLE alert_record
(
    id          BIGINT       NOT NULL COMMENT '告警记录id，用于唯一标识每条告警记录',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该告警记录的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该记录的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录记录生成的时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录最后一次更新该记录的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录最后一次更新该记录的时间',
    alert_time  BIGINT       NULL COMMENT '告警时间，记录告警触发的具体时间（使用时间戳格式）',
    details     VARCHAR(255) NULL COMMENT '告警详情，记录告警的具体描述和相关信息',
    level       VARCHAR(255) NULL COMMENT '告警严重度（1-5），表示告警的严重等级，数值范围1至5',
    name        VARCHAR(255) NULL COMMENT '告警名称，用于描述或标识告警的类型',
    read_flg    BIT          NULL COMMENT '是否已读，标识告警记录是否已被查看（1：已读，0：未读）',
    tenant_id   BIGINT       NULL COMMENT '租户ID，用于标识记录所属的租户，支持多租户环境',
    uid         VARCHAR(255) NULL COMMENT '配置所属用户，记录该告警记录对应的用户标识',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='存储系统产生的各类告警记录，便于历史记录查询和告警信息分析';


-- 文件名称: category.sql
-- 文件描述: 此SQL文件用于创建存储系统中分类信息的表 category。表中记录了分类的基本信息，
--         包括分类ID、名称、以及创建与更新时间等信息，同时支持多租户环境。
-- 使用场景: 当系统需要对数据进行分类管理时，该表用于存储各分类的基础信息，以便在查询、统计或业务逻辑处理中使用。
-- tag: 租户分类

CREATE TABLE category
(
    id          VARCHAR(255) NOT NULL COMMENT '分类id，作为主键用于唯一标识每个分类',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该分类的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该分类的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录分类记录的生成时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录最后一次修改该分类记录的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录最后一次修改该分类记录的时间',
    create_at   BIGINT       NULL COMMENT '分类描述，建议确认该字段是否用于描述分类（数据类型为 BIGINT 可能不适合描述性文本）',
    name        VARCHAR(255) NULL COMMENT '分类名称，记录分类的名称或标题',
    tenant_id   BIGINT       NULL COMMENT '租户ID，用于标识分类所属的租户，支持多租户系统',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='存储系统中各类分类的基本信息，便于数据管理和分类查询';


-- 文件名称: channel.sql
-- 文件描述: 此SQL文件用于创建存储通道相关信息的表 channel。
--         表中记录了通道的基本属性，包括通道ID、创建与更新时间、通道名称、图标、标题等，
--         同时支持多租户环境。该表可用于区分不同的功能模块或数据流，便于系统管理与展示。
-- 使用场景: 在系统中需要根据通道配置实现不同的业务逻辑或界面展示时，使用该表存储通道信息，
--         方便查询和管理。
-- tag: 租户通道

CREATE TABLE channel
(
    id          BIGINT       NOT NULL COMMENT '通道id，主键，用于唯一标识每个通道',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该通道记录的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该通道记录的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录通道记录生成的时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录最后一次更新该通道记录的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录最后一次更新该通道记录的时间',
    code        VARCHAR(255) NULL COMMENT '通道名称，用于标识或引用通道',
    create_at   BIGINT       NULL COMMENT '创建时间戳，用于记录精确的创建时间（与 create_time 可能存在重复）',
    icon        VARCHAR(255) NULL COMMENT '图标，存储通道对应的图标路径或标识，便于界面展示',
    tenant_id   BIGINT       NULL COMMENT '租户ID，用于标识记录所属的租户，支持多租户系统',
    title       VARCHAR(255) NULL COMMENT '标题，用于描述或展示通道的名称信息',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='存储系统中各通道的基本信息，便于管理、配置与展示不同的通道';


-- 文件名称: channel_config.sql
-- 文件描述: 此SQL文件用于创建存储通道配置信息的表 channel_config。
--         表中记录了通道的相关配置，包括通道ID、参数、创建时间等信息，
--         方便系统管理和动态调整通道参数。
-- 使用场景: 当系统中的通道（channel）需要配置不同的参数时，该表存储这些配置信息，
--         便于查询、管理和动态调整。
-- tag: 租户通道配置

CREATE TABLE channel_config
(
    id          BIGINT       NOT NULL COMMENT '通道配置id，主键，用于唯一标识每个通道配置',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该通道配置的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该通道配置的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录通道配置的生成时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录最后一次更新该通道配置的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录最后一次更新该通道配置的时间',
    channel_id  BIGINT       NULL COMMENT '通道id，外键，关联 channel 表中的通道，标识该配置所属的通道',
    create_at   BIGINT       NULL COMMENT '创建时间戳，可能用于记录精确的创建时间（与 create_time 可能存在重复）',
    param       TEXT         NULL COMMENT '通道配置参数，存储通道的具体配置信息（JSON、XML等格式）',
    tenant_id   BIGINT       NULL COMMENT '租户ID，用于标识记录所属的租户，支持多租户系统',
    title       VARCHAR(255) NULL COMMENT '通道配置名称，用于描述或标识该配置',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='存储通道的配置信息，包括通道关联、参数和基本信息，便于管理与动态调整';


-- 文件名称: channel_template.sql
-- 文件描述: 此SQL文件用于创建存储通道模板的表 channel_template。
--         该表用于定义通道的模板内容，允许用户根据通道配置定义不同的模板格式，
--         以支持不同的业务场景。
-- 使用场景: 当通道（channel）需要不同的模板以适应多种业务需求时，该表存储这些模板信息，
--         便于查询、管理和使用。

CREATE TABLE channel_template
(
    id                BIGINT       NOT NULL COMMENT '通道模板id，主键，用于唯一标识每个通道模板',
    create_by         BIGINT       NULL COMMENT '创建者，记录创建该通道模板的用户ID',
    create_dept       BIGINT       NULL COMMENT '创建部门，记录创建该通道模板的部门ID',
    create_time       DATETIME     NULL COMMENT '创建时间，记录通道模板的生成时间',
    update_by         BIGINT       NULL COMMENT '更新者，记录最后一次更新该通道模板的用户ID',
    update_time       DATETIME     NULL COMMENT '更新时间，记录最后一次更新该通道模板的时间',
    channel_config_id BIGINT       NULL COMMENT '通道配置id，外键，关联 channel_config 表，表示该模板基于某个通道配置',
    content           VARCHAR(255) NULL COMMENT '通道模板内容，存储模板的具体内容或格式（可扩展为 TEXT 类型以存储更长的内容）',
    create_at         BIGINT       NULL COMMENT '创建时间戳，可能用于记录精确的创建时间（与 create_time 可能存在重复）',
    tenant_id         BIGINT       NULL COMMENT '租户ID，用于标识记录所属的租户，支持多租户系统',
    title             VARCHAR(255) NULL COMMENT '通道模板名称，用于描述或标识该模板',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='存储通道的模板信息，包括模板内容、关联的通道配置等，便于业务使用不同模板格式';


-- 文件名称: device_config.sql
-- 文件描述: 此SQL文件用于创建存储设备配置信息的表 device_config。
--         该表用于记录设备的配置信息，包括设备的ID、名称、产品Key及其JSON格式的配置内容，
--         以支持设备管理和远程配置。
-- 使用场景: 当系统需要对不同的设备进行参数配置或远程管理时，该表存储设备的配置数据，
--         便于查询、管理和动态更新。

CREATE TABLE device_config
(
    id          VARCHAR(255) NOT NULL COMMENT '设备配置id，主键，用于唯一标识每个设备的配置',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该设备配置的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该设备配置的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录设备配置的生成时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录最后一次更新该设备配置的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录最后一次更新该设备配置的时间',
    config      TEXT         NULL COMMENT '设备配置JSON内容，存储设备的参数配置（建议存储 JSON 格式数据）',
    create_at   BIGINT       NULL COMMENT '创建时间戳，可能用于记录精确的创建时间（与 create_time 可能存在重复）',
    device_id   VARCHAR(255) NULL COMMENT '设备id，外键，关联设备表中的设备，标识该配置属于哪个设备',
    device_name VARCHAR(255) NULL COMMENT '设备名称，用于标识或描述设备的名称',
    product_key VARCHAR(255) NULL COMMENT '产品key，唯一标识设备所属的产品类别',
    tenant_id   BIGINT       NULL COMMENT '租户ID，用于标识记录所属的租户，支持多租户系统',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='存储设备的配置信息，包括设备ID、名称、产品Key及其配置信息，支持设备远程管理和配置更新';


-- 文件名称: device_group.sql
-- 文件描述: 此SQL文件用于创建存储设备分组信息的表 device_group。
--         该表用于管理多个设备的分组信息，支持批量管理设备。
--         设备组用于归类管理多个设备，便于批量操作和权限控制。
-- 使用场景: 当系统需要对多个设备进行分组管理时，该表存储设备组的相关信息，
--         便于查询、管理和操作不同分组的设备。

CREATE TABLE device_group
(
    id          VARCHAR(255) NOT NULL COMMENT '设备组id，主键，用于唯一标识每个设备组',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该设备组的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该设备组的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录设备组的生成时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录最后一次更新该设备组的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录最后一次更新该设备组的时间',
    create_at   BIGINT       NOT NULL COMMENT '创建时间戳，可能用于记录精确的创建时间（与 create_time 可能存在重复）',
    device_qty  INT          NOT NULL COMMENT '设备数量，记录该设备组下的设备总数',
    name        VARCHAR(255) NULL COMMENT '设备组名称，用于标识或描述设备组',
    remark      VARCHAR(255) NULL COMMENT '分组说明，存储该设备组的描述信息',
    tenant_id   BIGINT       NULL COMMENT '租户ID，用于标识记录所属的租户，支持多租户系统',
    uid         VARCHAR(255) NULL COMMENT '所属用户，记录设备组归属的用户ID',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='存储设备的分组信息，包括设备数量、名称和说明，支持设备批量管理和权限控制';


-- 文件名称: device_group_mapping.sql
-- 文件描述: 此SQL文件用于创建设备与设备组之间的映射关系表 device_group_mapping。
--         该表用于维护设备和设备组之间的多对多关系，每条记录表示一个设备属于某个设备组。
-- 使用场景: 当系统需要支持设备分组管理时，该表用于存储设备与设备组的关联信息，
--         便于查询设备所属的分组，或查询某个分组下的设备列表。

CREATE TABLE device_group_mapping
(
    id          VARCHAR(255) NOT NULL COMMENT '设备组映射id，主键，用于唯一标识每条设备与设备组的关系',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该映射关系的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该映射关系的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录设备组映射关系的创建时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录最后一次更新该映射关系的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录最后一次更新该映射关系的时间',
    device_id   VARCHAR(255) NULL COMMENT '设备id，外键，关联 device 表，表示该设备所属的设备组',
    group_id    VARCHAR(255) NULL COMMENT '设备组id，外键，关联 device_group 表，表示该分组包含的设备',
    tenant_id   BIGINT       NULL COMMENT '租户ID，用于标识记录所属的租户，支持多租户系统',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='存储设备与设备组的关联信息，支持设备分组管理和批量操作';


-- 文件名称: device_info.sql
-- 文件描述: 此SQL文件用于创建设备信息表 device_info。
--         该表用于存储设备的基本信息，包括设备的ID、名称、地理位置、离线，在线状态及相关的时间信息。
-- 使用场景: 该表适用于设备管理系统，可用于查询设备的基本信息、在线状态、所属租户及用户。

CREATE TABLE device_info
(
    id           VARCHAR(255) NOT NULL COMMENT '设备信息ID，主键，用于唯一标识每台设备',
    create_by    BIGINT       NULL COMMENT '创建者，记录创建该设备信息的用户ID',
    create_dept  BIGINT       NULL COMMENT '创建部门，记录创建该设备信息的部门ID',
    create_time  DATETIME     NULL COMMENT '创建时间，记录设备信息的创建时间',
    update_by    BIGINT       NULL COMMENT '更新者，记录最后一次更新该设备信息的用户ID',
    update_time  DATETIME     NULL COMMENT '更新时间，记录最后一次更新该设备信息的时间',
    create_at    BIGINT       NULL COMMENT '创建时间戳，可能用于记录精确的创建时间（与 create_time 可能存在重复）',
    device_id    VARCHAR(255) NULL COMMENT '设备ID，外键，关联 device 表，标识该设备的唯一标识',
    device_name  VARCHAR(255) NULL COMMENT '设备名称，存储设备的具体名称，便于识别',
    latitude     VARCHAR(255) NULL COMMENT '纬度，记录设备的地理位置信息',
    longitude    VARCHAR(255) NULL COMMENT '经度，记录设备的地理位置信息',
    model        VARCHAR(255) NULL COMMENT '设备类型，记录设备的型号或类别',
    offline_time BIGINT       NULL COMMENT '设备离线时间，记录设备最近一次离线的时间戳',
    online_time  BIGINT       NULL COMMENT '设备在线时间，记录设备最近一次上线的时间戳',
    parent_id    VARCHAR(255) NULL COMMENT '父级ID，表示该设备是否属于某个父设备（如网关设备）',
    product_key  VARCHAR(255) NULL COMMENT '产品Key，唯一标识设备所属的产品类别',
    secret       VARCHAR(255) NULL COMMENT '设备密钥，设备鉴权所需的密钥信息',
    state        VARCHAR(255) NULL COMMENT '设备状态，存储设备的当前状态（如在线、离线、故障）',
    tenant_id    BIGINT       NULL COMMENT '租户ID，用于标识记录所属的租户，支持多租户系统',
    uid          VARCHAR(255) NULL COMMENT '用户ID，记录设备的归属用户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='存储设备的基本信息，包括设备ID、名称、地理位置、状态及相关时间信息，支持设备管理和监控';


-- 文件名称: device_ota_detail.sql
-- 文件描述: 此SQL文件用于创建设备OTA（固件升级）详情表 device_ota_detail。
--         该表用于存储设备的OTA升级过程中的详细信息，包括设备ID、产品Key、升级任务ID、当前步骤等。
-- 使用场景: 当设备进行OTA升级时，该表用于跟踪升级进度，并存储相关的任务和设备信息。

CREATE TABLE device_ota_detail
(
    id          BIGINT       NOT NULL COMMENT '设备OTA详情ID，主键，用于唯一标识每条OTA升级记录',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该OTA升级记录的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该OTA升级记录的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录OTA升级记录的创建时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录最后一次更新该OTA升级记录的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录最后一次更新该OTA升级记录的时间',
    `desc`      VARCHAR(255) NULL COMMENT '升级描述，存储OTA升级的描述信息',
    device_id   VARCHAR(255) NULL COMMENT '设备ID，外键，关联 device 表，表示该升级对应的设备',
    device_name VARCHAR(255) NULL COMMENT '设备名称，存储设备的具体名称，便于识别',
    module      VARCHAR(255) NULL COMMENT '模块名称，标识设备的特定模块或组件（如Wi-Fi、主处理器等）',
    ota_info_id BIGINT       NULL COMMENT 'OTA信息ID，外键，关联 OTA 任务表，表示该升级属于哪个OTA任务',
    product_key VARCHAR(255) NULL COMMENT '产品Key，唯一标识设备所属的产品类别',
    step        INT          NULL COMMENT '升级进度步骤，标识设备OTA升级的当前进度（如0-未开始，1-下载中，2-升级中，3-完成等）',
    task_id     VARCHAR(255) NULL COMMENT 'OTA任务ID，标识该升级任务的唯一标识',
    tenant_id   BIGINT       NULL COMMENT '租户ID，用于标识记录所属的租户，支持多租户系统',
    version     VARCHAR(255) NULL COMMENT '设备固件版本号，记录设备当前或即将升级的固件版本',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='存储设备OTA（固件升级）的详细信息，支持设备的远程固件升级管理和进度跟踪';


-- 文件名称: device_ota_info.sql
-- 文件描述: 该SQL文件用于创建设备OTA（固件升级）任务表 device_ota_info。
--         该表用于存储OTA升级任务的整体信息，如升级的目标设备数、成功/失败统计等。
-- 使用场景: 该表用于管理设备的OTA升级任务，每个任务可以包含多个设备的升级过程。

CREATE TABLE device_ota_info
(
    id          BIGINT       NOT NULL COMMENT 'OTA任务ID，主键，唯一标识每个OTA升级任务',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该OTA升级任务的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该OTA升级任务的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录OTA任务的创建时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录最后一次更新该OTA升级任务的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录最后一次更新该OTA升级任务的时间',
    create_at   BIGINT       NULL COMMENT '任务创建时间戳，记录任务的精确创建时间',
    `desc`      VARCHAR(255) NULL COMMENT '任务描述，存储OTA升级任务的简要说明',
    fail        INT          NULL COMMENT '失败设备数，记录在此OTA任务中升级失败的设备数量',
    module      VARCHAR(255) NULL COMMENT '模块名称，标识本次OTA升级的具体模块（如Wi-Fi、主处理器等）',
    package_id  BIGINT       NULL COMMENT '升级包ID，外键，指向存储的OTA固件包',
    product_key VARCHAR(255) NULL COMMENT '产品Key，唯一标识设备所属的产品类别',
    success     INT          NULL COMMENT '成功设备数，记录本次OTA任务中升级成功的设备数量',
    tenant_id   BIGINT       NULL COMMENT '租户ID，用于标识该OTA任务属于哪个租户，支持多租户系统',
    total       INT          NULL COMMENT '总设备数，记录参与此OTA任务的设备总数量',
    version     VARCHAR(255) NULL COMMENT '目标固件版本号，表示本次OTA任务要升级的版本',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='设备OTA（固件升级）任务表，记录OTA任务的基本信息和升级统计数据';


-- 文件名称: device_sub_user.sql
-- 文件描述: 该SQL文件用于创建设备子用户表 device_sub_user。
--         该表用于存储与设备关联的子用户信息，包括设备与子用户之间的关联关系。
-- 使用场景: 当设备与多个用户关联时，每个用户在设备上的角色信息可以存储在该表中。

CREATE TABLE device_sub_user
(
    id          VARCHAR(255) NOT NULL COMMENT '子用户关联记录ID，主键，唯一标识每个设备与子用户的关联关系',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该子用户关联关系的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该子用户关联关系的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录该子用户关联关系的创建时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录最后一次更新该子用户关联关系的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录最后一次更新该子用户关联关系的时间',
    device_id   VARCHAR(255) NULL COMMENT '设备ID，外键，指向设备表，表示该子用户关联的设备',
    tenant_id   BIGINT       NULL COMMENT '租户ID，用于标识记录所属的租户，支持多租户系统',
    uid         VARCHAR(255) NULL COMMENT '设备用户ID，标识与设备关联的子用户的唯一标识',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='设备子用户关联表，记录设备与子用户之间的关系，支持多用户管理设备';


-- 文件名称: device_tag.sql
-- 文件描述: 该SQL文件用于创建设备标签表 device_tag。
--         该表用于存储设备的扩展标签信息，支持为设备添加自定义属性标签。
-- 使用场景: 当设备需要支持动态扩展属性时（如传感器类型、设备位置等），可通过标签机制灵活存储键值对数据。

CREATE TABLE device_tag
(
    id          VARCHAR(255) NOT NULL COMMENT '主键ID，唯一标识标签记录，建议使用UUID或雪花算法生成',
    create_by   BIGINT       NULL COMMENT '创建者用户ID，外键关联用户表(user.id)',
    create_dept BIGINT       NULL COMMENT '创建部门ID，外键关联部门表(dept.id)',
    create_time DATETIME     NULL COMMENT '记录创建时间（UTC时区），格式: YYYY-MM-DD HH:MM:SS',
    update_by   BIGINT       NULL COMMENT '最后更新者用户ID，外键关联用户表(user.id)',
    update_time DATETIME     NULL COMMENT '最后更新时间（UTC时区），格式: YYYY-MM-DD HH:MM:SS',
    code        VARCHAR(255) NULL COMMENT '标签业务编码（需保证唯一性），如 TEMPERATURE_SENSOR',
    device_id   VARCHAR(255) NULL COMMENT '外键关联设备表(device.id)，标识标签所属设备',
    name        VARCHAR(255) NULL COMMENT '标签展示名称（如中文名称），如 温度传感器',
    tenant_id   BIGINT       NULL COMMENT '租户ID，外键关联租户表(tenant.id)，实现多租户数据隔离',
    value       VARCHAR(255) NULL COMMENT '标签值，存储实际业务数据（如 36.5），单位在业务逻辑中定义',
    constraint `PRIMARY`
        primary key (id)
) COMMENT='设备标签表，存储设备的自定义属性标签。'
  '核心设计说明：'
  '1. 通过(code,value)实现设备属性的动态扩展'
  '2. 支持多租户数据隔离，不同租户标签互不可见'
  '3. 建议设备删除时同步清理关联标签（可通过外键级联删除实现）';

-- 文件名称: home.sql
-- 文件描述: 该SQL文件用于创建智能家庭管理表 home。
--         该表用于存储家庭基础信息及设备空间元数据，支持多租户家庭体系管理。
-- 使用场景: 用户创建智能家庭时，存储家庭地址、设备数量、空间数量等核心数据，并标识用户当前使用的家庭。

CREATE TABLE home
(
    id          BIGINT       NOT NULL COMMENT '主键ID，唯一标识家庭记录，建议使用雪花算法生成',
    create_by   BIGINT       NULL COMMENT '创建者用户ID，外键关联用户表(user.id)',
    create_dept BIGINT       NULL COMMENT '创建部门ID，外键关联部门表(dept.id)',
    create_time DATETIME     NULL COMMENT '记录创建时间（UTC时区），格式: YYYY-MM-DD HH:MM:SS',
    update_by   BIGINT       NULL COMMENT '最后更新者用户ID，外键关联用户表(user.id)',
    update_time DATETIME     NULL COMMENT '最后更新时间（UTC时区），格式: YYYY-MM-DD HH:MM:SS',
    address     VARCHAR(255) NULL COMMENT '家庭物理地址，格式: 国家+省市区+详细地址，如 中国北京市海淀区xx路10号',
    current     BIT          NULL COMMENT '当前使用标识（1:是 0:否），每个用户最多有1个当前家庭',
    device_num  INT          NULL COMMENT '设备总数（需通过触发器或应用逻辑维护，与device表实时同步）',
    name        VARCHAR(255) NULL COMMENT '家庭名称（用户自定义），如 幸福之家',
    space_num   INT          NULL COMMENT '空间总数（需通过space表统计维护，如客厅/卧室等）',
    tenant_id   BIGINT       NULL COMMENT '租户ID，外键关联租户表(tenant.id)，实现多租户数据隔离',
    user_id     BIGINT       NULL COMMENT '所属用户ID，外键关联用户表(user.id)，标识家庭管理员',
    constraint `PRIMARY`
        primary key (id)
) COMMENT='家庭核心元数据表，管理智能家庭基础信息。'
  '核心设计说明：'
  '1. 通过device_num/space_num实现快速统计，需确保与关联表数据一致性'
  '2. current字段逻辑需配合用户维度唯一约束（如唯一索引uniq_user_current）'
  '3. 建议级联删除：用户删除时同步清理家庭数据';

-- 文件名称: icon.sql
-- 文件描述: 该SQL文件用于创建图标表 icon。
--         该表用于存储系统中的图标信息，支持图标内容、分类、版本等管理。
-- 使用场景: 该表适用于图标的存储管理，可用于支持图标展示的应用程序、管理平台等。

CREATE TABLE icon
(
    id           BIGINT       NOT NULL COMMENT '图标ID，主键，唯一标识每个图标记录',
    create_by    BIGINT       NULL COMMENT '创建者，记录创建该图标的用户ID',
    create_dept  BIGINT       NULL COMMENT '创建部门，记录创建该图标的部门ID',
    create_time  DATETIME     NULL COMMENT '创建时间，记录图标的创建时间',
    update_by    BIGINT       NULL COMMENT '更新者，记录最后一次更新该图标的用户ID',
    update_time  DATETIME     NULL COMMENT '更新时间，记录最后一次更新该图标的时间',
    icon_content TEXT         NULL COMMENT '图标内容，存储图标的具体数据或内容（如SVG代码等）',
    icon_name    VARCHAR(255) NULL COMMENT '图标名称，标识图标的名称',
    icon_type_id BIGINT       NULL COMMENT '图标分类ID，外键，指向图标分类表，表示该图标的类型或类别',
    tenant_id    BIGINT       NULL COMMENT '租户ID，用于标识图标所属的租户，支持多租户系统',
    version      VARCHAR(255) NULL COMMENT '图标版本，标识该图标的版本信息',
    view_box     VARCHAR(255) NULL COMMENT '视窗缩放，图标视窗的属性（如SVG中的viewBox属性）',
    xmlns        VARCHAR(255) NULL COMMENT '命名空间，图标内容的命名空间（如SVG的xmlns属性）',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='图标表，存储图标的详细信息，包括名称、内容、版本、视窗属性等';


-- 文件名称: icon_type.sql
-- 文件描述: 该SQL文件用于创建图标分类表 icon_type。
--         该表用于存储图标的分类信息，如图标所属的类型（例如系统图标、用户自定义图标等）。
-- 使用场景: 该表适用于图标的分类管理，方便对图标进行归类管理。

CREATE TABLE icon_type
(
    id            BIGINT       NOT NULL COMMENT '主键ID，唯一标识每个图标分类记录',
    create_by     BIGINT       NULL COMMENT '创建者，记录创建该图标分类的用户ID',
    create_dept   BIGINT       NULL COMMENT '创建部门，记录创建该图标分类的部门ID',
    create_time   DATETIME     NULL COMMENT '创建时间，记录图标分类的创建时间',
    update_by     BIGINT       NULL COMMENT '更新者，记录最后一次更新该图标分类的用户ID',
    update_time   DATETIME     NULL COMMENT '更新时间，记录最后一次更新该图标分类的时间',
    tenant_id     BIGINT       NULL COMMENT '租户ID，用于标识图标分类所属的租户，支持多租户系统',
    type_describe VARCHAR(255) NULL COMMENT '分类描述，描述该图标分类的含义或用途',
    type_name     VARCHAR(255) NULL COMMENT '分类名称，标识图标分类的名称，例如“系统图标”、“自定义图标”',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='图标分类表，存储不同类型图标的分类信息，便于对图标进行分组管理';


-- 文件名称: modbus_info.sql
-- 文件描述: 该SQL文件用于创建Modbus设备信息表 modbus_info。
--         该表用于存储Modbus设备的配置信息，包括产品名称、productKey、用户、租户等信息。
-- 使用场景: 该表适用于Modbus设备的管理，记录与Modbus协议相关的设备信息。

CREATE TABLE modbus_info
(
    id          BIGINT       NOT NULL COMMENT '主键ID，唯一标识每个Modbus设备的配置信息',
    create_at   BIGINT       NULL COMMENT '创建时间，记录Modbus设备配置的创建时间',
    name        VARCHAR(255) NULL COMMENT '产品名称，标识Modbus设备的名称',
    product_key VARCHAR(255) NULL COMMENT '产品Key，用于唯一标识Modbus设备，通常与设备的身份和权限关联',
    remark      VARCHAR(255) NULL COMMENT '说明，提供关于该Modbus设备的一些备注或描述信息',
    tenant_id   BIGINT       NULL COMMENT '租户ID，标识该Modbus设备配置所属的租户，支持多租户系统',
    uid         VARCHAR(255) NULL COMMENT '配置所属用户ID，标识与该Modbus设备配置相关的用户',
    update_at   BIGINT       NULL COMMENT '更新时间，记录Modbus设备配置的最后更新时间',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='Modbus设备信息表，存储Modbus设备的配置信息，包括设备名称、productKey、所属用户等';


-- 文件名称: modbus_thing_model.sql
-- 文件描述: 该SQL文件用于创建Modbus设备模型表 modbus_thing_model。
--         该表用于存储与Modbus设备相关的设备模型信息，包括模型内容、产品Key、租户等信息。
-- 使用场景: 该表适用于Modbus设备模型的管理，记录每个设备的具体模型配置，帮助与设备交互。

CREATE TABLE modbus_thing_model
(
    id          BIGINT       NOT NULL COMMENT '主键，唯一标识每个Modbus设备模型',
    model       TEXT         NULL COMMENT '模型内容，包含Modbus设备的详细模型配置，通常是JSON或类似格式的配置数据',
    product_key VARCHAR(255) NULL COMMENT '产品Key，用于唯一标识Modbus设备，通常与设备身份和权限关联',
    tenant_id   BIGINT       NULL COMMENT '租户ID，标识该Modbus设备模型所属的租户，支持多租户系统',
    update_at   BIGINT       NULL COMMENT '更新时间，记录Modbus设备模型的最后更新时间',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='Modbus设备模型表，存储与Modbus设备相关的设备模型配置，包括模型内容、产品Key等信息';


-- 文件名称: notify_message.sql
-- 文件描述: 该SQL文件用于创建通知消息表 notify_message。
--         该表用于存储系统发送的通知消息信息，包括消息内容、消息类型、状态等。
-- 使用场景: 该表适用于存储系统生成的通知消息，用于提醒用户或系统管理者，支持多种消息类型和状态管理。

CREATE TABLE notify_message
(
    id           BIGINT       NOT NULL COMMENT '通知消息ID，唯一标识每条通知消息',
    create_by    BIGINT       NULL COMMENT '创建者，记录该通知消息的创建者用户ID',
    create_dept  BIGINT       NULL COMMENT '创建部门，记录该通知消息所属的创建部门ID',
    create_time  DATETIME     NULL COMMENT '创建时间，记录通知消息的创建时间',
    update_by    BIGINT       NULL COMMENT '更新者，记录最后一次更新该通知消息的用户ID',
    update_time  DATETIME     NULL COMMENT '更新时间，记录最后一次更新通知消息的时间',
    content      VARCHAR(255) NULL COMMENT '消息内容，存储该通知消息的详细信息或正文',
    create_at    BIGINT       NULL COMMENT '创建时间的时间戳，提供系统中的精确创建时间',
    message_type VARCHAR(255) NULL COMMENT '消息类型，标识该通知消息的类型（如警告、信息、错误等）',
    status       BIT          NULL COMMENT '消息状态，表示该消息是否已读或已处理（0-未读，1-已读等）',
    tenant_id    BIGINT       NULL COMMENT '租户ID，用于标识该通知消息所属的租户，支持多租户系统',
    update_at    BIGINT       NULL COMMENT '更新时间的时间戳，记录最后更新时间的精确时间',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='通知消息表，存储系统生成的通知消息，包括消息内容、类型、状态等';


-- 文件名称: oauth_client.sql
-- 文件描述: 该SQL文件用于创建OAuth客户端表 oauth_client。
--         该表用于存储OAuth客户端相关信息，包括客户端ID、密钥、允许访问的URL等。
-- 使用场景: 该表适用于OAuth认证系统，用于存储和管理授权的客户端信息，以支持OAuth授权流程。

CREATE TABLE oauth_client
(
    id            VARCHAR(255) NOT NULL COMMENT '唯一标识每个OAuth客户端的ID',
    create_by     BIGINT       NULL COMMENT '创建者，记录该OAuth客户端信息的创建者用户ID',
    create_dept   BIGINT       NULL COMMENT '创建部门，记录该OAuth客户端信息所属的创建部门ID',
    create_time   DATETIME     NULL COMMENT '创建时间，记录该OAuth客户端信息的创建时间',
    update_by     BIGINT       NULL COMMENT '更新者，记录最后一次更新该OAuth客户端信息的用户ID',
    update_time   DATETIME     NULL COMMENT '更新时间，记录最后一次更新OAuth客户端信息的时间',
    allow_url     VARCHAR(255) NULL COMMENT '允许访问的URL，指定OAuth客户端能够访问的URL列表，通常是授权回调URL',
    client_id     VARCHAR(255) NULL COMMENT '客户端ID，用于唯一标识OAuth客户端，通常用于OAuth认证流程中进行身份验证',
    client_secret VARCHAR(255) NULL COMMENT '客户端密钥，用于OAuth认证中的客户端验证，确保只有授权的客户端可以访问资源',
    create_at     BIGINT       NULL COMMENT '创建时间的时间戳，提供系统中的精确创建时间',
    name          VARCHAR(255) NULL COMMENT '客户端名称，用于描述该OAuth客户端的名称，通常为易于理解的标识',
    tenant_id     BIGINT       NULL COMMENT '租户ID，标识该OAuth客户端所属的租户，支持多租户系统',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='OAuth客户端表，存储OAuth认证系统中注册的客户端信息，包括客户端ID、密钥、允许的访问URL等';


-- 文件名称: oper_log.sql
-- 文件描述: 该SQL文件用于创建操作日志表 oper_log。
--         该表用于记录系统中的各种操作日志，包含操作的详细信息，如操作人员、操作内容、请求参数等。
-- 使用场景: 适用于任何需要记录操作日志的系统，支持业务审计、性能监控和错误排查。

CREATE TABLE oper_log
(
    id             BIGINT        NOT NULL COMMENT '日志主键，唯一标识每一条日志记录',
    business_type  INT           NULL COMMENT '业务类型，区分不同的操作类型 (0 其它, 1 新增, 2 修改, 3 删除)',
    cost_time      BIGINT        NULL COMMENT '消耗时间，记录操作执行的时间长度（单位：毫秒）',
    dept_name      VARCHAR(255)  NULL COMMENT '部门名称，记录执行操作的部门名称',
    error_msg      VARCHAR(2000) NULL COMMENT '错误消息，若操作发生错误，记录错误详细信息',
    json_result    VARCHAR(2000) NULL COMMENT '返回参数，记录操作执行后的返回结果，以JSON格式存储',
    method         VARCHAR(255)  NULL COMMENT '请求方法，记录被调用的方法名称',
    oper_ip        VARCHAR(255)  NULL COMMENT '操作地址，记录操作的IP地址',
    oper_location  VARCHAR(255)  NULL COMMENT '操作地点，记录操作发生的地理位置或设备信息',
    oper_name      VARCHAR(255)  NULL COMMENT '操作人员，记录执行该操作的人员名称',
    oper_param     VARCHAR(2000) NULL COMMENT '请求参数，记录发起请求时携带的参数，以JSON格式存储',
    oper_time      DATETIME      NULL COMMENT '操作时间，记录具体的操作发生时间',
    oper_url       VARCHAR(255)  NULL COMMENT '请求URL，记录请求的URL地址',
    operator_type  INT           NULL COMMENT '操作类别，区分操作的发起者 (0 其它, 1 后台用户, 2 手机端用户)',
    request_method VARCHAR(255)  NULL COMMENT '请求方式，记录请求的HTTP方法（GET, POST等）',
    status         INT           NULL COMMENT '操作状态，记录操作的状态 (0 正常, 1 异常)',
    tenant_id      BIGINT        NULL COMMENT '租户编号，标识操作所属的租户',
    title          VARCHAR(255)  NULL COMMENT '操作模块，记录操作所属的模块名称',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='操作日志表，用于记录系统中所有用户和管理员的操作记录，支持审计、监控和问题排查';


-- 文件名称: ota_device.sql
-- 文件描述: 该SQL文件用于创建OTA设备表 ota_device。
--         该表用于记录设备的OTA（Over-The-Air）升级信息，包括设备状态、版本、创建时间等。
-- 使用场景: 适用于设备管理系统中，记录与设备相关的OTA升级信息，支持设备的远程管理、升级和状态跟踪。

CREATE TABLE ota_device
(
    id          BIGINT       NOT NULL COMMENT '主键id，唯一标识每一条OTA设备记录',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该设备记录的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该设备记录的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录设备记录的创建时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录更新该设备记录的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录设备记录的最后更新时间',
    create_at   BIGINT       NULL COMMENT '设备创建时间，记录设备的初次创建时间（Unix时间戳）',
    device_id   VARCHAR(255) NULL COMMENT '设备ID，唯一标识设备',
    device_name VARCHAR(255) NULL COMMENT '设备名称，记录设备的名称或描述',
    status      INT          NULL COMMENT '设备状态，表示设备的当前状态，如0为离线，1为在线',
    tenant_id   BIGINT       NULL COMMENT '租户ID，标识该设备所属的租户',
    version     VARCHAR(255) NULL COMMENT '设备版本，记录设备的当前软件版本',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='OTA设备表，记录设备的OTA升级信息和状态，包括设备的创建、更新和版本信息';


-- 文件名称: ota_package.sql
-- 文件描述: 该SQL文件用于创建OTA升级包表 ota_package。
--         该表用于记录OTA升级包的信息，包括包的版本、大小、MD5值、URL等。
-- 使用场景: 适用于设备管理系统中，存储和管理OTA升级包的信息，确保设备能够通过OTA升级到指定的版本。

CREATE TABLE ota_package
(
    id          BIGINT       NOT NULL COMMENT '主键id，唯一标识每一条OTA升级包记录',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该OTA包记录的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该OTA包记录的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录OTA包记录的创建时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录更新该OTA包记录的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录OTA包记录的最后更新时间',
    create_at   BIGINT       NULL COMMENT 'OTA包创建时间，记录OTA包的创建时间（Unix时间戳）',
    `desc`      VARCHAR(255) NULL COMMENT 'OTA包描述，描述OTA包的内容和用途',
    ext_data    VARCHAR(255) NULL COMMENT '扩展数据，存储额外信息，如兼容设备等',
    is_diff     BIT          NULL COMMENT '是否为差分包，0表示不是差分包，1表示是差分包',
    md5         VARCHAR(255) NULL COMMENT 'OTA包的MD5校验值，用于验证包的完整性',
    module      VARCHAR(255) NULL COMMENT 'OTA包的模块，表示该包包含的模块或功能',
    name        VARCHAR(255) NULL COMMENT 'OTA包名称，描述该包的名称或版本标识',
    product_key VARCHAR(255) NULL COMMENT '产品key，标识该包属于哪个产品',
    sign        VARCHAR(255) NULL COMMENT '签名，OTA包的签名用于确保包的合法性',
    sign_method VARCHAR(255) NULL COMMENT '签名方法，描述使用的签名算法或方式',
    size        BIGINT       NULL COMMENT 'OTA包的大小，以字节为单位',
    tenant_id   BIGINT       NULL COMMENT '租户ID，标识该OTA包所属的租户',
    url         VARCHAR(255) NULL COMMENT 'OTA包的下载链接，用于设备获取包文件',
    version     VARCHAR(255) NULL COMMENT 'OTA包的版本号，标识该OTA包的版本',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='OTA升级包表，存储OTA包的详细信息，包括包的版本、大小、MD5值等';


-- 文件名称: plugin_info.sql
-- 文件描述: 该SQL文件用于创建插件信息表 plugin_info。
--         该表用于记录插件信息，包括插件名称、配置、版本、部署方式等。
-- 使用场景: 适用于设备管理系统中，存储和管理设备插件的信息，支持插件的配置、部署、版本管理等功能。

CREATE TABLE plugin_info
(
    id            BIGINT       NOT NULL COMMENT '插件信息主键id，唯一标识每一条插件记录',
    create_by     BIGINT       NULL COMMENT '创建者，记录创建该插件记录的用户ID',
    create_dept   BIGINT       NULL COMMENT '创建部门，记录创建该插件记录的部门ID',
    create_time   DATETIME     NULL COMMENT '创建时间，记录插件信息记录的创建时间',
    update_by     BIGINT       NULL COMMENT '更新者，记录更新该插件记录的用户ID',
    update_time   DATETIME     NULL COMMENT '更新时间，记录插件信息记录的最后更新时间',
    config        TEXT         NULL COMMENT '插件配置信息，存储插件的配置信息，如参数等',
    config_schema TEXT         NULL COMMENT '插件配置项描述信息，描述插件配置信息的结构和规则',
    deploy_type   VARCHAR(255) NULL COMMENT '部署方式，描述插件的部署方式，如单机、集群等',
    description   VARCHAR(255) NULL COMMENT '插件描述，描述插件的功能和用途',
    file          VARCHAR(255) NULL COMMENT '插件包地址，存储插件包文件的下载路径或位置',
    name          VARCHAR(255) NULL COMMENT '插件名称，标识插件的名称',
    plugin_id     VARCHAR(255) NULL COMMENT '插件包id，标识该插件的唯一标识符',
    protocol      VARCHAR(255) NULL COMMENT '设备插件协议类型，描述插件支持的协议类型',
    script        TEXT         NULL COMMENT '插件脚本，存储插件的脚本内容或路径',
    state         VARCHAR(255) NULL COMMENT '插件状态，描述插件的当前状态，如启用、禁用等',
    tenant_id     BIGINT       NULL COMMENT '租户编号，标识该插件所属的租户',
    type          VARCHAR(255) NULL COMMENT '插件类型，描述插件的类别，如设备插件、数据处理插件等',
    version       VARCHAR(255) NULL COMMENT '插件版本，记录插件的版本号',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='插件信息表，存储设备插件的详细信息，包括插件的配置、版本、部署方式等';


-- 文件名称: plugin_instance.sql
-- 文件描述: 该SQL文件用于创建插件实例表 plugin_instance。
--         该表用于记录插件实例的信息，包括插件的主程序ID、心跳时间、IP地址、端口等。
-- 使用场景: 适用于设备管理系统中，存储和管理插件实例的状态信息，支持插件实例的生命周期管理。

CREATE TABLE plugin_instance
(
    id           BIGINT       NOT NULL COMMENT '插件实例ID，唯一标识每一条插件实例记录',
    create_by    BIGINT       NULL COMMENT '创建者，记录创建该插件实例记录的用户ID',
    create_dept  BIGINT       NULL COMMENT '创建部门，记录创建该插件实例记录的部门ID',
    create_time  DATETIME     NULL COMMENT '创建时间，记录插件实例记录的创建时间',
    update_by    BIGINT       NULL COMMENT '更新者，记录更新该插件实例记录的用户ID',
    update_time  DATETIME     NULL COMMENT '更新时间，记录插件实例记录的最后更新时间',
    heartbeat_at BIGINT       NULL COMMENT '心跳时间，记录插件实例的最后心跳时间（Unix时间戳）',
    ip           VARCHAR(255) NULL COMMENT '插件主程序所在IP地址，记录插件实例所在的服务器IP',
    main_id      VARCHAR(255) NULL COMMENT '插件主程序ID，标识插件主程序的唯一标识符',
    plugin_id    BIGINT       NULL COMMENT '插件ID，关联插件信息表中的插件ID',
    port         INT          NOT NULL COMMENT '插件主程序端口，标识插件实例的端口号',
    tenant_id    BIGINT       NULL COMMENT '租户ID，标识该插件实例所属的租户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='插件实例表，存储插件实例的状态信息，包括插件的主程序ID、心跳时间、IP地址、端口等';


-- 文件名称: product.sql
-- 文件描述: 该SQL文件用于创建产品表 product。
--         该表用于记录产品的信息，包括产品名称、密钥、图标、定位等。
-- 使用场景: 适用于设备管理系统中，存储和管理产品信息，确保产品的唯一标识和属性的统一管理。

CREATE TABLE product
(
    id                 BIGINT       NOT NULL COMMENT '产品ID，唯一标识每一条产品记录',
    create_by          BIGINT       NULL COMMENT '创建者，记录创建该产品记录的用户ID',
    create_dept        BIGINT       NULL COMMENT '创建部门，记录创建该产品记录的部门ID',
    create_time        DATETIME     NULL COMMENT '创建时间，记录产品记录的创建时间',
    update_by          BIGINT       NULL COMMENT '更新者，记录更新该产品记录的用户ID',
    update_time        DATETIME     NULL COMMENT '更新时间，记录产品记录的最后更新时间',
    category           VARCHAR(255) NULL COMMENT '品类，表示产品所属的分类或类型',
    create_at          BIGINT       NULL COMMENT '产品创建时间，记录产品的创建时间（Unix时间戳）',
    icon_id            BIGINT       NULL COMMENT '产品图标ID，关联到图标表中的图标ID',
    img                VARCHAR(255) NULL COMMENT '产品图片，记录产品的相关图片链接',
    is_open_locate     BIT          NULL COMMENT '是否开启设备定位，true表示开启，false表示关闭',
    keep_alive_time    BIGINT       NULL COMMENT '保活时长（秒），表示设备的保活时间，单位为秒',
    locate_update_type VARCHAR(255) NULL COMMENT '定位更新方式，记录定位更新的具体策略或方式',
    name               VARCHAR(255) NULL COMMENT '产品名称，记录产品的名称',
    node_type          INT          NULL COMMENT '节点类型，标识产品节点的类型（如设备、传感器等）',
    product_key        VARCHAR(255) NULL COMMENT '产品key，唯一标识该产品',
    product_secret     VARCHAR(255) NULL COMMENT '产品密钥，用于产品身份验证',
    tenant_id          BIGINT       NULL COMMENT '租户ID，标识该产品所属的租户',
    transparent        BIT          NULL COMMENT '是否透传，true表示透传，false表示不透传',
    uid                VARCHAR(255) NULL COMMENT '用户ID，记录与该产品相关联的用户ID',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='产品表，存储产品的详细信息，包括产品名称、密钥、图标、定位等';


-- 文件名称: product_model.sql
-- 文件描述: 该SQL文件用于创建产品型号表 product_model。
--         该表用于记录产品的型号、脚本内容、产品Key等信息。
-- 使用场景: 适用于设备管理系统中，存储和管理产品型号的信息，确保型号和产品之间的关联及管理。

CREATE TABLE product_model
(
    id          VARCHAR(255) NOT NULL COMMENT '型号ID，唯一标识每一条型号记录',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该型号记录的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该型号记录的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录型号记录的创建时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录更新该型号记录的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录型号记录的最后更新时间',
    model       VARCHAR(255) NULL COMMENT '型号，表示产品的型号',
    modify_at   BIGINT       NULL COMMENT '修改时间，记录型号的最后修改时间（Unix时间戳）',
    name        VARCHAR(255) NULL COMMENT '名称，记录型号的名称',
    product_key VARCHAR(255) NULL COMMENT '产品Key，标识该型号对应的产品',
    script      TEXT         NULL COMMENT '脚本内容，存储与该型号相关的脚本信息',
    state       VARCHAR(255) NULL COMMENT '脚本状态，表示脚本当前的状态（例如：启用、禁用）',
    tenant_id   BIGINT       NULL COMMENT '租户ID，标识该型号所属的租户',
    type        VARCHAR(255) NULL COMMENT '脚本类型，表示脚本的类型（例如：初始化、更新等）',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='产品型号表，存储产品型号的详细信息，包括型号、脚本内容、产品Key等';


-- 文件名称: rule_info.sql
-- 文件描述: 该SQL文件用于创建规则信息表 rule_info。
--         该表用于记录规则的详细信息，包括规则的动作、过滤器、监听器等。
-- 使用场景: 适用于事件驱动系统中，管理和存储规则的相关信息，包括触发规则时执行的动作和条件。

CREATE TABLE rule_info
(
    id          VARCHAR(255) NOT NULL COMMENT '规则ID，唯一标识每一条规则记录',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该规则记录的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该规则记录的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录规则记录的创建时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录更新该规则记录的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录规则记录的最后更新时间',
    actions     TEXT         NULL COMMENT '动作，描述规则触发时需要执行的操作或动作',
    create_at   BIGINT       NULL COMMENT '规则创建时间，记录规则的创建时间（Unix时间戳）',
    `desc`      VARCHAR(255) NULL COMMENT '描述，描述该规则的功能和用途',
    filters     TEXT         NULL COMMENT '过滤器，定义规则应用的条件',
    listeners   TEXT         NULL COMMENT '监听器，描述规则触发时的事件监听器',
    name        VARCHAR(255) NULL COMMENT '规则名称，标识该规则的名称',
    state       VARCHAR(255) NULL COMMENT '状态，表示规则当前的状态（如启用、禁用等）',
    tenant_id   BIGINT       NULL COMMENT '租户ID，标识该规则所属的租户',
    type        VARCHAR(255) NULL COMMENT '规则类型，表示规则的类型（例如：业务规则、系统规则等）',
    uid         VARCHAR(255) NULL COMMENT '用户ID，表示该规则所属的用户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='规则信息表，存储规则的详细信息，包括动作、过滤器、监听器等';


-- 文件名称: screen.sql
-- 文件描述: 该SQL文件用于创建屏幕信息表 screen。
--         该表用于记录屏幕的详细信息，包括屏幕名称、端口、资源文件等。
-- 使用场景: 适用于屏幕管理系统中，存储和管理屏幕相关的信息，如显示设置、状态等。

CREATE TABLE screen
(
    id            BIGINT       NOT NULL COMMENT '主键id，唯一标识每一条屏幕记录',
    create_at     BIGINT       NULL COMMENT '创建时间，记录屏幕的创建时间（Unix时间戳）',
    is_default    BIT          NULL COMMENT '是否为默认屏幕，0表示不是默认，1表示是默认屏幕',
    name          VARCHAR(255) NULL COMMENT '屏幕名称，标识该屏幕的名称',
    port          INT          NULL COMMENT '端口号，标识屏幕的端口配置',
    resource_file VARCHAR(255) NULL COMMENT '资源文件路径，存储屏幕所需的资源文件',
    state         VARCHAR(255) NULL COMMENT '屏幕状态，表示屏幕当前的状态（如启用、禁用等）',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='屏幕信息表，存储屏幕的详细信息，包括屏幕名称、端口、资源文件等';


-- 文件名称: screen_api.sql
-- 文件描述: 该SQL文件用于创建屏幕API表 screen_api。
--         该表用于记录与屏幕相关的API信息，包括API路径、请求方法、参数等。
-- 使用场景: 适用于屏幕管理系统中，管理与屏幕交互的API接口信息，便于处理屏幕数据的交互与请求。

CREATE TABLE screen_api
(
    id          BIGINT       NOT NULL COMMENT '主键id，唯一标识每一条屏幕API记录',
    api_params  VARCHAR(255) NULL COMMENT 'API请求参数，描述API接口的请求参数',
    api_path    VARCHAR(255) NULL COMMENT 'API路径，指定该API接口的路径',
    create_at   BIGINT       NULL COMMENT '创建时间，记录API的创建时间（Unix时间戳）',
    data_source VARCHAR(255) NULL COMMENT '数据源，指明API请求数据来源（如数据库、外部服务等）',
    http_method VARCHAR(255) NULL COMMENT 'HTTP请求方法，描述API接口的请求方法（GET、POST、PUT等）',
    screen_id   BIGINT       NULL COMMENT '屏幕ID，关联到具体的屏幕记录',
    script      TEXT         NULL COMMENT '脚本内容，存储与API接口相关的执行脚本',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='屏幕API表，存储与屏幕相关的API信息，包括API路径、请求方法、参数等';


-- 文件名称: space.sql
-- 文件描述: 该SQL文件用于创建空间表 space。
--         该表用于记录空间的信息，包括空间名称、设备数量、关联家庭等。
-- 使用场景: 适用于家庭管理系统或物联网应用系统，管理家庭中的各个空间及其设备。

CREATE TABLE space
(
    id          BIGINT       NOT NULL COMMENT '主键id，唯一标识每一个空间',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该空间记录的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该空间记录的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录空间信息的创建时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录更新该空间记录的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录空间信息的最后更新时间',
    device_num  INT          NULL COMMENT '设备数量，记录该空间中包含的设备数量',
    home_id     BIGINT       NULL COMMENT '关联家庭id，记录该空间属于哪个家庭',
    name        VARCHAR(255) NULL COMMENT '空间名称，描述该空间的名称',
    tenant_id   BIGINT       NULL COMMENT '租户编号，标识该空间所属的租户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='空间表，存储空间的相关信息，包括空间名称、设备数量、关联家庭等';

-- 文件名称: space_device.sql
-- 文件描述: 该SQL文件用于创建空间设备表 space_device。
--         该表用于记录空间中设备的信息，包括设备ID、设备名称、是否收藏等。
-- 使用场景: 适用于家庭管理系统或物联网应用系统，管理设备与空间的关联信息。

CREATE TABLE space_device
(
    id          BIGINT       NOT NULL COMMENT '主键id，唯一标识每一个空间中的设备',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该设备记录的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该设备记录的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录设备信息的创建时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录更新该设备记录的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录设备信息的最后更新时间',
    collect     BIT          NULL COMMENT '是否收藏，表示该设备是否被标记为收藏',
    device_id   VARCHAR(255) NULL COMMENT '设备ID，记录设备的唯一标识',
    home_id     BIGINT       NULL COMMENT '所属家庭ID，记录设备属于哪个家庭',
    name        VARCHAR(255) NULL COMMENT '设备名称，描述设备的名称',
    space_id    BIGINT       NULL COMMENT '空间ID，记录设备所在的空间ID',
    tenant_id   BIGINT       NULL COMMENT '租户编号，标识该设备所属的租户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='空间设备表，存储设备与空间的关联信息，包括设备ID、设备名称、是否收藏等';


-- 文件名称: sys_app.sql
-- 文件描述: 该SQL文件用于创建系统应用表 sys_app。
--         该表用于记录系统应用的信息，包括应用的ID、名称、类型、秘钥等。
-- 使用场景: 适用于管理系统中的应用信息，例如记录接入的第三方应用、系统内嵌的应用等。

CREATE TABLE sys_app
(
    id          BIGINT       NOT NULL COMMENT '主键id，唯一标识每一个系统应用',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该应用记录的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该应用记录的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录应用信息的创建时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录更新该应用记录的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录应用信息的最后更新时间',
    app_id      VARCHAR(255) NULL COMMENT '应用ID，记录应用的唯一标识',
    app_name    VARCHAR(255) NULL COMMENT '应用名称，描述该应用的名称',
    app_secret  VARCHAR(255) NULL COMMENT '应用秘钥，用于验证该应用的合法性',
    app_type    VARCHAR(255) NULL COMMENT '应用类型，描述该应用的类型（如：Web、Mobile等）',
    remark      VARCHAR(255) NULL COMMENT '备注，记录有关该应用的附加信息',
    tenant_id   BIGINT       NULL COMMENT '租户编号，标识该应用所属的租户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='系统应用表，存储系统应用的信息，包括应用ID、名称、类型、秘钥等';


-- 文件名称: sys_config.sql
-- 文件描述: 该SQL文件用于创建系统配置表 sys_config。
--         该表用于存储系统中的配置信息，包括参数的键名、键值、类型等。
-- 使用场景: 适用于存储系统的配置信息，用于系统初始化配置、动态配置更新等场景。

CREATE TABLE sys_config
(
    id           BIGINT       NOT NULL COMMENT '参数主键，唯一标识每一条配置记录',
    create_by    BIGINT       NULL COMMENT '创建者，记录创建该配置记录的用户ID',
    create_dept  BIGINT       NULL COMMENT '创建部门，记录创建该配置记录的部门ID',
    create_time  DATETIME     NULL COMMENT '创建时间，记录配置信息的创建时间',
    update_by    BIGINT       NULL COMMENT '更新者，记录更新该配置记录的用户ID',
    update_time  DATETIME     NULL COMMENT '更新时间，记录配置信息的最后更新时间',
    config_key   VARCHAR(255) NULL COMMENT '参数键名，唯一标识该配置项的名称',
    config_name  VARCHAR(255) NULL COMMENT '参数名称，描述该配置项的含义',
    config_type  VARCHAR(255) NULL COMMENT '系统内置（Y是 N否），标识该配置是否为系统内置',
    config_value VARCHAR(255) NULL COMMENT '参数键值，配置项的实际值',
    remark       VARCHAR(255) NULL COMMENT '备注，记录有关该配置项的附加信息',
    tenant_id    BIGINT       NULL COMMENT '租户编号，标识该配置项所属的租户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='系统配置表，存储系统的配置信息，包括参数的键名、键值、类型等';


-- 文件名称: sys_dept.sql
-- 文件描述: 该SQL文件用于创建部门表 sys_dept。
--         该表用于记录系统中的部门信息，包括部门名称、负责人、联系电话等。
-- 使用场景: 适用于企业系统、组织管理系统等，记录各个部门的信息及层级结构。

CREATE TABLE sys_dept
(
    id          BIGINT       NOT NULL COMMENT '部门ID，唯一标识每个部门',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该部门的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该部门的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录部门的创建时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录更新该部门的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录部门的最后更新时间',
    ancestors   VARCHAR(255) NULL COMMENT '祖级列表，记录部门的上级部门路径',
    del_flag    VARCHAR(255) NULL COMMENT '删除标志（0代表存在 2代表删除）',
    dept_name   VARCHAR(255) NULL COMMENT '部门名称，描述部门的名称',
    email       VARCHAR(255) NULL COMMENT '邮箱，部门的联系邮箱',
    leader      VARCHAR(255) NULL COMMENT '负责人，部门的负责人',
    order_num   INT          NULL COMMENT '显示顺序，部门在列表中的显示顺序',
    parent_id   BIGINT       NULL COMMENT '父部门ID，记录该部门所属的上级部门ID',
    phone       VARCHAR(255) NULL COMMENT '联系电话，部门的联系电话',
    status      VARCHAR(255) NULL COMMENT '部门状态：0正常,1停用，表示部门的当前状态',
    tenant_id   BIGINT       NULL COMMENT '租户ID，标识该部门所属的租户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='部门表，记录系统中的部门信息，包括部门名称、负责人、联系电话等';


-- 文件名称: sys_dict_data.sql
-- 文件描述: 该SQL文件用于创建字典数据表 sys_dict_data。
--         该表用于存储字典数据，包含字典标签、字典类型、字典键值等信息。
-- 使用场景: 适用于系统中需要进行字典管理的场景，如枚举类型、分类数据等。

CREATE TABLE sys_dict_data
(
    id          BIGINT       NOT NULL COMMENT '字典编码，唯一标识每条字典记录',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该字典数据的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该字典数据的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录字典数据的创建时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录更新该字典数据的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录字典数据的最后更新时间',
    css_class   VARCHAR(255) NULL COMMENT '样式属性（其他样式扩展），用于在前端展示时的样式控制',
    dict_label  VARCHAR(255) NULL COMMENT '字典标签，表示字典数据的标签名称',
    dict_sort   INT          NULL COMMENT '字典排序，表示字典数据的显示顺序',
    dict_type   VARCHAR(255) NULL COMMENT '字典类型，表示字典数据所属的类型，如性别、状态等',
    dict_value  VARCHAR(255) NULL COMMENT '字典键值，字典的具体值',
    is_default  VARCHAR(255) NULL COMMENT '是否默认（Y是 N否），标识是否为默认字典项',
    list_class  VARCHAR(255) NULL COMMENT '表格字典样式，表格展示时的样式类别',
    remark      VARCHAR(255) NULL COMMENT '备注，记录字典数据的附加信息',
    status      VARCHAR(255) NULL COMMENT '状态（0正常 1停用），标识字典数据的当前状态',
    tenant_id   BIGINT       NULL COMMENT '租户编号，标识该字典数据所属的租户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='字典数据表，存储系统中的字典信息，如字典标签、类型、键值、排序等';


-- 文件名称: sys_dict_type.sql
-- 文件描述: 该SQL文件用于创建字典类型表 sys_dict_type。
--         该表用于存储字典的类型信息，包括字典名称、字典类型、状态等。
-- 使用场景: 适用于系统中管理字典类型的场景，如分类管理、枚举类型等。

CREATE TABLE sys_dict_type
(
    id          BIGINT       NOT NULL COMMENT '字典主键，唯一标识每一条字典类型记录',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该字典类型的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该字典类型的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录字典类型的创建时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录更新该字典类型的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录字典类型的最后更新时间',
    dict_name   VARCHAR(255) NULL COMMENT '字典名称，表示字典类型的名称',
    dict_type   VARCHAR(255) NULL COMMENT '字典类型，表示该字典项的类型（如性别、状态等）',
    remark      VARCHAR(255) NULL COMMENT '备注，记录字典类型的附加信息',
    status      VARCHAR(255) NULL COMMENT '状态（0正常 1停用），表示字典类型的当前状态',
    tenant_id   BIGINT       NULL COMMENT '租户编号，标识该字典类型所属的租户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='字典类型表，存储系统中的字典类型信息，如字典名称、字典类型、状态等';


-- 文件名称: sys_logininfor.sql
-- 文件描述: 该SQL文件用于创建登录信息表 sys_logininfor。
--         该表用于记录用户的登录信息，包括登录时间、IP地址、浏览器类型、操作系统等。
-- 使用场景: 适用于系统中记录用户登录日志的场景，便于审计和分析用户登录活动。

CREATE TABLE sys_logininfor
(
    id             BIGINT       NOT NULL COMMENT 'ID，唯一标识每一条登录记录',
    create_by      BIGINT       NULL COMMENT '创建者，记录创建该登录记录的用户ID',
    create_dept    BIGINT       NULL COMMENT '创建部门，记录创建该登录记录的部门ID',
    create_time    DATETIME     NULL COMMENT '创建时间，记录登录记录的创建时间',
    update_by      BIGINT       NULL COMMENT '更新者，记录更新该登录记录的用户ID',
    update_time    DATETIME     NULL COMMENT '更新时间，记录登录记录的最后更新时间',
    browser        VARCHAR(255) NULL COMMENT '浏览器类型，记录用户使用的浏览器信息',
    ipaddr         VARCHAR(255) NULL COMMENT '登录IP地址，记录用户登录时的IP地址',
    login_location VARCHAR(255) NULL COMMENT '登录地点，记录用户登录的物理地点',
    login_time     DATETIME     NULL COMMENT '访问时间，记录用户登录的具体时间',
    msg            VARCHAR(255) NULL COMMENT '提示消息，记录登录的相关提示信息',
    os             VARCHAR(255) NULL COMMENT '操作系统，记录用户登录时使用的操作系统',
    status         VARCHAR(255) NULL COMMENT '登录状态（0成功，1失败），表示登录是否成功',
    tenant_id      BIGINT       NULL COMMENT '租户编号，标识该登录记录所属的租户',
    user_name      VARCHAR(255) NULL COMMENT '用户账号，记录用户的登录账号',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='登录信息表，存储用户登录日志，包括登录时间、IP地址、浏览器类型等信息';


-- 文件名称: sys_menu.sql
-- 文件描述: 该SQL文件用于创建菜单表 sys_menu。
--         该表用于记录系统菜单的信息，包括菜单名称、类型、权限、路由等。
-- 使用场景: 适用于系统中菜单管理的场景，便于记录和管理系统中的各类菜单。

CREATE TABLE sys_menu
(
    menu_id     BIGINT       NOT NULL COMMENT '菜单ID，唯一标识每个菜单',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该菜单的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该菜单的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录菜单的创建时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录更新该菜单的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录菜单的最后更新时间',
    component   VARCHAR(255) NULL COMMENT '组件路径，记录与菜单关联的组件路径',
    icon        VARCHAR(255) NULL COMMENT '菜单图标，记录菜单的图标信息',
    is_cache    VARCHAR(255) NULL COMMENT '是否缓存（0缓存，1不缓存），记录菜单是否启用缓存',
    is_frame    VARCHAR(255) NULL COMMENT '是否为外链（0是，1否），标记该菜单是否为外部链接',
    menu_name   VARCHAR(255) NULL COMMENT '菜单名称，记录菜单的名称',
    menu_type   VARCHAR(255) NULL COMMENT '类型（M目录，C菜单，F按钮），标记菜单类型',
    order_num   INT          NULL COMMENT '显示顺序，记录菜单显示的顺序',
    parent_id   BIGINT       NULL COMMENT '父菜单ID，记录该菜单的上级菜单ID',
    path        VARCHAR(255) NULL COMMENT '路由地址，记录菜单对应的路由地址',
    perms       VARCHAR(255) NULL COMMENT '权限字符串，记录与该菜单相关联的权限',
    query_param VARCHAR(255) NULL COMMENT '路由参数，记录路由需要的参数',
    remark      VARCHAR(255) NULL COMMENT '备注，记录额外的信息或说明',
    status      VARCHAR(255) NULL COMMENT '菜单状态（0正常，1停用），标记该菜单是否启用',
    visible     VARCHAR(255) NULL COMMENT '显示状态（0显示，1隐藏），记录菜单的显示状态',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (menu_id)
) COMMENT='菜单表，记录系统菜单的详细信息，包括菜单名称、类型、路由、权限等';


-- 文件名称: sys_notice.sql
-- 文件描述: 该SQL文件用于创建公告表 sys_notice。
--         该表用于记录系统公告的信息，包括公告内容、类型、状态等。
-- 使用场景: 适用于记录和管理系统中的公告信息。

CREATE TABLE sys_notice
(
    id             BIGINT       NOT NULL COMMENT '公告ID，唯一标识每个公告',
    create_by      BIGINT       NULL COMMENT '创建者，记录创建该公告的用户ID',
    create_dept    BIGINT       NULL COMMENT '创建部门，记录创建该公告的部门ID',
    create_time    DATETIME     NULL COMMENT '创建时间，记录公告的创建时间',
    update_by      BIGINT       NULL COMMENT '更新者，记录更新该公告的用户ID',
    update_time    DATETIME     NULL COMMENT '更新时间，记录公告的最后更新时间',
    notice_content VARCHAR(255) NULL COMMENT '公告内容，记录公告的详细内容',
    notice_title   VARCHAR(255) NULL COMMENT '公告标题，记录公告的标题',
    notice_type    VARCHAR(255) NULL COMMENT '公告类型（1通知，2公告），标记公告的类型',
    remark         VARCHAR(255) NULL COMMENT '备注，记录额外的信息或说明',
    status         VARCHAR(255) NULL COMMENT '公告状态（0正常，1关闭），标记该公告的状态',
    tenant_id      BIGINT       NULL COMMENT '租户编号，标记该公告所属的租户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='公告表，记录系统公告的详细信息，包括公告内容、类型、状态等';


-- 文件名称: sys_oss.sql
-- 文件描述: 该SQL文件用于创建对象存储表 sys_oss。
--         该表用于记录对象存储的信息，包括文件名、后缀名、服务商等。
-- 使用场景: 适用于记录和管理系统中使用的对象存储信息。

CREATE TABLE sys_oss
(
    id            BIGINT       NOT NULL COMMENT '对象存储主键，唯一标识每个对象存储记录',
    create_by     BIGINT       NULL COMMENT '创建者，记录创建该存储记录的用户ID',
    create_dept   BIGINT       NULL COMMENT '创建部门，记录创建该存储记录的部门ID',
    create_time   DATETIME     NULL COMMENT '创建时间，记录对象存储记录的创建时间',
    update_by     BIGINT       NULL COMMENT '更新者，记录更新该存储记录的用户ID',
    update_time   DATETIME     NULL COMMENT '更新时间，记录对象存储记录的最后更新时间',
    file_name     VARCHAR(255) NULL COMMENT '文件名，记录存储对象的文件名',
    file_suffix   VARCHAR(255) NULL COMMENT '文件后缀名，记录存储对象的文件类型后缀',
    original_name VARCHAR(255) NULL COMMENT '原名，记录上传前的文件原名',
    service       VARCHAR(255) NULL COMMENT '服务商，标记使用的对象存储服务商',
    tenant_id     BIGINT       NULL COMMENT '租户编号，标记该存储记录所属的租户',
    url           VARCHAR(255) NULL COMMENT 'URL地址，记录对象存储的访问地址',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='对象存储表，用于记录系统中存储的文件信息，包括文件名、后缀名、服务商等';


-- 文件名称: sys_oss_config.sql
-- 文件描述: 该SQL文件用于创建对象存储配置表 sys_oss_config。
--         该表用于记录和管理与对象存储相关的配置信息，如桶名称、访问密钥、权限设置等。
-- 使用场景: 适用于管理系统中对象存储配置的信息，并确保能根据配置与对象存储服务进行交互。

CREATE TABLE sys_oss_config
(
    id            BIGINT       NOT NULL COMMENT '主键，唯一标识每条配置记录',
    create_by     BIGINT       NULL COMMENT '创建者，记录创建该配置的用户ID',
    create_dept   BIGINT       NULL COMMENT '创建部门，记录创建该配置的部门ID',
    create_time   DATETIME     NULL COMMENT '创建时间，记录对象存储配置的创建时间',
    update_by     BIGINT       NULL COMMENT '更新者，记录更新该配置的用户ID',
    update_time   DATETIME     NULL COMMENT '更新时间，记录对象存储配置的最后更新时间',
    access_key    VARCHAR(255) NULL COMMENT 'AccessKey，记录对象存储的访问密钥',
    access_policy VARCHAR(255) NULL COMMENT '桶权限类型（0：private，1：public，2：custom）',
    bucket_name   VARCHAR(255) NULL COMMENT '桶名称，记录对象存储桶的名称',
    config_key    VARCHAR(255) NULL COMMENT '配置Key，用于标识存储配置',
    domain        VARCHAR(255) NULL COMMENT '自定义域名，记录访问存储的域名',
    endpoint      VARCHAR(255) NULL COMMENT '访问站点，记录存储的访问URL',
    ext1          VARCHAR(255) NULL COMMENT '扩展字段，用于存储其他附加信息',
    is_https      VARCHAR(255) NULL COMMENT '是否启用HTTPS（0：否，1：是）',
    prefix        VARCHAR(255) NULL COMMENT '前缀，记录存储文件的前缀路径',
    region        VARCHAR(255) NULL COMMENT '域，记录存储桶所在的地域',
    remark        VARCHAR(255) NULL COMMENT '备注，记录该配置的附加说明',
    secret_key    VARCHAR(255) NULL COMMENT 'SecretKey，记录对象存储的访问密钥',
    status        VARCHAR(255) NULL COMMENT '是否默认（0：是，1：否）',
    tenant_id     BIGINT       NULL COMMENT '租户编号，标记该存储配置所属的租户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='对象存储配置表，用于记录和管理对象存储相关配置信息';


-- 文件名称: sys_post.sql
-- 文件描述: 该SQL文件用于创建岗位表 sys_post。
--         该表用于记录和管理系统中的岗位信息，如岗位编码、岗位名称、岗位排序等。
-- 使用场景: 适用于管理岗位信息，包含创建、更新岗位的相关字段。

CREATE TABLE sys_post
(
    id          BIGINT       NOT NULL COMMENT '岗位序号，唯一标识每个岗位',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该岗位的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该岗位的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录岗位信息的创建时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录更新该岗位的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录岗位信息的最后更新时间',
    post_code   VARCHAR(255) NULL COMMENT '岗位编码，用于唯一标识岗位',
    post_name   VARCHAR(255) NULL COMMENT '岗位名称，记录岗位的名称',
    post_sort   INT          NULL COMMENT '岗位排序，用于设置岗位显示顺序',
    remark      VARCHAR(255) NULL COMMENT '备注，记录岗位的附加说明',
    status      VARCHAR(255) NULL COMMENT '岗位状态（0正常 1停用）',
    tenant_id   BIGINT       NULL COMMENT '租户编号，标识该岗位所属的租户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='岗位表，用于记录和管理系统中的岗位信息，如岗位编码、岗位名称、排序等';


-- 文件名称: sys_role.sql
-- 文件描述: 该SQL文件用于创建角色表 sys_role。
--         该表用于记录和管理系统中的角色信息，如角色名称、角色权限、角色排序等。
-- 使用场景: 适用于管理角色信息，包含角色权限、角色名称、角色排序、角色状态等字段。

CREATE TABLE sys_role
(
    id                  BIGINT       NOT NULL COMMENT '角色ID，唯一标识每个角色',
    create_by           BIGINT       NULL COMMENT '创建者，记录创建该角色的用户ID',
    create_dept         BIGINT       NULL COMMENT '创建部门，记录创建该角色的部门ID',
    create_time         DATETIME     NULL COMMENT '创建时间，记录角色信息的创建时间',
    update_by           BIGINT       NULL COMMENT '更新者，记录更新该角色的用户ID',
    update_time         DATETIME     NULL COMMENT '更新时间，记录角色信息的最后更新时间',
    data_scope          VARCHAR(255) NULL COMMENT '数据范围（1：所有数据权限；2：自定义数据权限；3：本部门数据权限；4：本部门及以下数据权限；5：仅本人数据权限）',
    del_flag            VARCHAR(255) NULL COMMENT '删除标志（0代表存在 2代表删除）',
    dept_check_strictly BIT          NULL COMMENT '部门树选择项是否关联显示（0：父子不互相关联显示 1：父子互相关联显示）',
    menu_check_strictly BIT          NULL COMMENT '菜单树选择项是否关联显示（0：父子不互相关联显示 1：父子互相关联显示）',
    remark              VARCHAR(255) NULL COMMENT '备注，记录角色的附加说明',
    role_key            VARCHAR(255) NULL COMMENT '角色权限，用于标识角色的权限',
    role_name           VARCHAR(255) NULL COMMENT '角色名称，记录角色的名称',
    role_sort           INT          NULL COMMENT '角色排序，用于设置角色显示顺序',
    status              VARCHAR(255) NULL COMMENT '角色状态（0正常 1停用）',
    tenant_id           BIGINT       NULL COMMENT '租户编号，标识该角色所属的租户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='角色表，用于记录和管理系统中的角色信息，如角色名称、角色权限、角色排序等';


-- 文件名称: sys_role_dept.sql
-- 文件描述: 该SQL文件用于创建角色与部门的关联表 sys_role_dept。
--         该表用于记录系统中角色与部门的关联关系。
-- 使用场景: 适用于管理角色与部门之间的关系，便于角色分配给不同部门。

CREATE TABLE sys_role_dept
(
    id          BIGINT   NOT NULL COMMENT '主键，唯一标识每条角色与部门的关联记录',
    create_by   BIGINT   NULL COMMENT '创建者，记录创建该关联关系的用户ID',
    create_dept BIGINT   NULL COMMENT '创建部门，记录创建该关联关系的部门ID',
    create_time DATETIME NULL COMMENT '创建时间，记录角色与部门关联关系的创建时间',
    update_by   BIGINT   NULL COMMENT '更新者，记录更新该关联关系的用户ID',
    update_time DATETIME NULL COMMENT '更新时间，记录角色与部门关联关系的最后更新时间',
    dept_id     BIGINT   NULL COMMENT '部门ID，表示该角色所属的部门',
    role_id     BIGINT   NULL COMMENT '角色ID，表示该部门关联的角色',
    tenant_id   BIGINT   NULL COMMENT '租户编号，标识该角色与部门关联关系所属的租户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='角色与部门的关联表，用于记录角色与部门之间的关系';


-- 文件名称: sys_role_menu.sql
-- 文件描述: 该SQL文件用于创建角色与菜单的关联表 sys_role_menu。
--         该表用于记录系统中角色与菜单的关联关系。
-- 使用场景: 适用于管理角色与菜单之间的关系，便于角色拥有不同的菜单权限。

CREATE TABLE sys_role_menu
(
    id          BIGINT   NOT NULL COMMENT '主键，唯一标识每条角色与菜单的关联记录',
    create_by   BIGINT   NULL COMMENT '创建者，记录创建该关联关系的用户ID',
    create_dept BIGINT   NULL COMMENT '创建部门，记录创建该关联关系的部门ID',
    create_time DATETIME NULL COMMENT '创建时间，记录角色与菜单关联关系的创建时间',
    update_by   BIGINT   NULL COMMENT '更新者，记录更新该关联关系的用户ID',
    update_time DATETIME NULL COMMENT '更新时间，记录角色与菜单关联关系的最后更新时间',
    menu_id     BIGINT   NULL COMMENT '菜单ID，表示该角色关联的菜单',
    role_id     BIGINT   NULL COMMENT '角色ID，表示该菜单关联的角色',
    tenant_id   BIGINT   NULL COMMENT '租户编号，标识该角色与菜单关联关系所属的租户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='角色与菜单的关联表，用于记录角色与菜单之间的关系';


-- 文件名称: sys_tenant.sql
-- 文件描述: 该SQL文件用于创建租户表 sys_tenant。
--         该表用于记录系统中的租户信息，如租户基本信息、账户数量、联系方式等。
-- 使用场景: 适用于多租户系统中管理各个租户的基本信息和状态。

CREATE TABLE sys_tenant
(
    id                BIGINT       NOT NULL COMMENT '租户的唯一标识id',
    create_by         BIGINT       NULL COMMENT '创建者，记录创建租户的用户ID',
    create_dept       BIGINT       NULL COMMENT '创建部门，记录创建租户的部门ID',
    create_time       DATETIME     NULL COMMENT '租户创建时间',
    update_by         BIGINT       NULL COMMENT '更新者，记录更新租户的用户ID',
    update_time       DATETIME     NULL COMMENT '租户最后更新时间',
    account_count     BIGINT       NULL COMMENT '用户数量（-1表示不限制用户数量）',
    address           VARCHAR(255) NULL COMMENT '租户地址',
    company_name      VARCHAR(255) NULL COMMENT '租户公司名称',
    contact_phone     VARCHAR(255) NULL COMMENT '联系人联系电话',
    contact_user_name VARCHAR(255) NULL COMMENT '联系人姓名',
    del_flag          VARCHAR(255) NULL COMMENT '删除标志（0代表存在，2代表删除）',
    domain            VARCHAR(255) NULL COMMENT '租户域名',
    expire_time       DATETIME     NULL COMMENT '租户过期时间',
    intro             VARCHAR(255) NULL COMMENT '租户简介',
    license_number    VARCHAR(255) NULL COMMENT '租户统一社会信用代码',
    package_id        BIGINT       NULL COMMENT '租户套餐编号',
    remark            VARCHAR(255) NULL COMMENT '备注',
    status            VARCHAR(255) NULL COMMENT '租户状态（0代表正常，1代表停用）',
    tenant_id         BIGINT       NULL COMMENT '租户编号',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='租户信息表，用于记录系统中的租户的基本信息、状态以及其他相关数据';


-- 文件名称: sys_tenant_package.sql
-- 文件描述: 该SQL文件用于创建租户套餐表 sys_tenant_package。
--         该表用于记录不同租户套餐的基本信息，包含套餐的名称、状态、关联菜单等。
-- 使用场景: 适用于多租户系统中管理租户套餐的功能。

CREATE TABLE sys_tenant_package
(
    id                  BIGINT       NOT NULL COMMENT '租户套餐唯一标识ID',
    create_by           BIGINT       NULL COMMENT '创建者，记录创建租户套餐的用户ID',
    create_dept         BIGINT       NULL COMMENT '创建部门，记录创建租户套餐的部门ID',
    create_time         DATETIME     NULL COMMENT '租户套餐创建时间',
    update_by           BIGINT       NULL COMMENT '更新者，记录更新租户套餐的用户ID',
    update_time         DATETIME     NULL COMMENT '租户套餐最后更新时间',
    del_flag            VARCHAR(255) NULL COMMENT '删除标志（0代表存在，2代表删除）',
    menu_check_strictly BIT          NULL COMMENT '菜单树选择项是否关联显示（0：父子不互相关联显示 1：父子互相关联显示）',
    menu_ids            TEXT         NULL COMMENT '关联菜单ID（存储菜单ID列表）',
    package_name        VARCHAR(255) NULL COMMENT '套餐名称',
    remark              VARCHAR(255) NULL COMMENT '备注',
    status              VARCHAR(255) NULL COMMENT '套餐状态（0正常，1停用）',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='租户套餐表，用于记录系统中各个租户套餐的基本信息、状态以及关联菜单等';


-- 文件名称: sys_user.sql
-- 文件描述: 该SQL文件用于创建用户表 sys_user。
--         该表用于记录系统中所有用户的基本信息，包括用户账号、密码、联系方式等。
-- 使用场景: 适用于多租户系统中管理用户信息的功能。

CREATE TABLE sys_user
(
    id          BIGINT       NOT NULL COMMENT '用户ID',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该用户的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该用户的部门ID',
    create_time DATETIME     NULL COMMENT '用户创建时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录更新该用户的用户ID',
    update_time DATETIME     NULL COMMENT '用户最后更新时间',
    avatar      BIGINT       NULL COMMENT '用户头像的ID',
    del_flag    VARCHAR(255) NULL COMMENT '删除标志（0代表存在，2代表删除）',
    dept_id     BIGINT       NULL COMMENT '用户所属部门ID',
    email       VARCHAR(255) NULL COMMENT '用户邮箱',
    login_date  DATETIME     NULL COMMENT '用户最后登录时间',
    login_ip    VARCHAR(255) NULL COMMENT '用户最后登录IP',
    nick_name   VARCHAR(255) NULL COMMENT '用户昵称',
    password    VARCHAR(255) NULL COMMENT '用户密码',
    phonenumber VARCHAR(255) NULL COMMENT '用户手机号码',
    remark      VARCHAR(255) NULL COMMENT '备注',
    sex         VARCHAR(255) NULL COMMENT '用户性别',
    status      VARCHAR(255) NULL COMMENT '帐号状态（0正常，1停用）',
    tenant_id   BIGINT       NULL COMMENT '租户编号',
    user_name   VARCHAR(255) NULL COMMENT '用户账号',
    user_type   VARCHAR(255) NULL COMMENT '用户类型（sys_user表示系统用户）',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='用户表，记录系统中所有用户的基本信息，如账号、密码、联系方式等';


-- 文件名称: sys_user_post.sql
-- 文件描述: 该SQL文件用于创建用户岗位关联表 sys_user_post。
--         该表用于记录用户和岗位之间的关联关系。
-- 使用场景: 适用于多租户系统中，管理用户与岗位的关系。

CREATE TABLE sys_user_post
(
    id          BIGINT   NOT NULL COMMENT '主键ID',
    create_by   BIGINT   NULL COMMENT '创建者，记录创建该关联的用户ID',
    create_dept BIGINT   NULL COMMENT '创建部门，记录创建该关联的部门ID',
    create_time DATETIME NULL COMMENT '创建时间',
    update_by   BIGINT   NULL COMMENT '更新者，记录更新该关联的用户ID',
    update_time DATETIME NULL COMMENT '更新时间',
    post_id     BIGINT   NULL COMMENT '岗位ID',
    tenant_id   BIGINT   NULL COMMENT '租户编号',
    user_id     BIGINT   NULL COMMENT '用户ID，表示用户与岗位的关联',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='用户与岗位的关联表，记录用户和岗位之间的关系';


-- 文件名称: sys_user_role.sql
-- 文件描述: 该SQL文件用于创建用户角色关联表 sys_user_role。
--         该表用于记录用户和角色之间的关联关系。
-- 使用场景: 适用于多租户系统中，管理用户与角色的关系。

CREATE TABLE sys_user_role
(
    id          BIGINT   NOT NULL COMMENT '主键ID',
    create_by   BIGINT   NULL COMMENT '创建者，记录创建该关联的用户ID',
    create_dept BIGINT   NULL COMMENT '创建部门，记录创建该关联的部门ID',
    create_time DATETIME NULL COMMENT '创建时间',
    update_by   BIGINT   NULL COMMENT '更新者，记录更新该关联的用户ID',
    update_time DATETIME NULL COMMENT '更新时间',
    role_id     BIGINT   NULL COMMENT '角色ID',
    tenant_id   BIGINT   NULL COMMENT '租户编号',
    user_id     BIGINT   NULL COMMENT '用户ID，表示用户和角色的关联',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='用户与角色的关联表，记录用户和角色之间的关系';

-- 文件名称: task_info.sql
-- 文件描述: 该SQL文件用于创建任务信息表 task_info。
--         该表用于记录任务的信息，包括任务的状态、描述、执行结果等。
-- 使用场景: 适用于任务管理和调度系统，用于存储和管理各类任务的执行情况。

CREATE TABLE task_info
(
    id          VARCHAR(255) NOT NULL COMMENT '主键，唯一标识每个任务',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该任务的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该任务的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录任务创建的时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录更新该任务的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录任务最后一次更新的时间',
    actions     TEXT         NULL COMMENT '任务输出，记录任务执行过程中的输出信息',
    create_at   BIGINT       NULL COMMENT '创建时间，记录任务创建的时间戳',
    `desc`      VARCHAR(255) NULL COMMENT '描述，简要描述任务的内容和目标',
    expression  VARCHAR(255) NULL COMMENT '表达式，任务的执行表达式或条件',
    name        VARCHAR(255) NULL COMMENT '任务名称，任务的唯一标识名',
    reason      VARCHAR(255) NULL COMMENT '操作备注，记录任务操作时的备注信息',
    state       VARCHAR(255) NULL COMMENT '任务状态，表示任务当前的状态',
    tenant_id   BIGINT       NULL COMMENT '租户编号，标识任务所属的租户',
    type        VARCHAR(255) NULL COMMENT '任务类型，表示任务的种类或类型',
    uid         VARCHAR(255) NULL COMMENT '创建者，记录任务创建者的标识',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='任务信息表，记录任务的基本信息和执行状态';


-- 文件名称: thing_model.sql
-- 文件描述: 该SQL文件用于创建产品模型表 thing_model。
--         该表用于记录产品模型的相关信息，包括模型内容和产品 key。
-- 使用场景: 适用于物联网设备管理系统，用于存储和管理设备模型的内容。

CREATE TABLE thing_model
(
    id          BIGINT       NOT NULL COMMENT '主键，唯一标识每个设备模型',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该模型的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该模型的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录模型创建的时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录更新该模型的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录模型最后一次更新的时间',
    model       TEXT         NULL COMMENT '模型内容，设备模型的详细定义和配置',
    product_key VARCHAR(255) NULL COMMENT '产品key，唯一标识产品的Key',
    tenant_id   BIGINT       NULL COMMENT '租户编号，标识模型所属的租户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='产品模型表，记录设备的模型内容和配置信息';


-- 文件名称: user_info.sql
-- 文件描述: 该SQL文件用于创建用户信息表 user_info。
--         该表用于存储用户的基本信息，包括联系方式、账户信息、角色及权限等。
-- 使用场景: 适用于用户管理系统，记录平台用户或终端用户的详细信息。

CREATE TABLE user_info
(
    id            BIGINT       NOT NULL COMMENT '主键ID，唯一标识每个用户',
    create_by     BIGINT       NULL COMMENT '创建者，记录创建该用户信息的用户ID',
    create_dept   BIGINT       NULL COMMENT '创建部门，记录创建该用户信息的部门ID',
    create_time   DATETIME     NULL COMMENT '创建时间，记录用户信息创建的时间',
    update_by     BIGINT       NULL COMMENT '更新者，记录更新该用户信息的用户ID',
    update_time   DATETIME     NULL COMMENT '更新时间，记录用户信息最后一次更新的时间',
    address       VARCHAR(255) NULL COMMENT '用户地址',
    avatar_url    VARCHAR(255) NULL COMMENT '用户头像地址',
    curr_home_id  VARCHAR(255) NULL COMMENT '当前家庭ID',
    email         VARCHAR(255) NULL COMMENT '用户邮箱',
    gender        INT          NULL COMMENT '用户性别（0-未知，1-男性，2-女性）',
    nick_name     VARCHAR(255) NULL COMMENT '用户昵称',
    permissions   VARCHAR(255) NULL COMMENT '用户权限',
    roles         VARCHAR(255) NULL COMMENT '用户角色',
    secret        VARCHAR(255) NULL COMMENT '用户密钥（密码加密后的内容）',
    tenant_id     BIGINT       NULL COMMENT '租户编号，标识该用户所属的租户',
    type          INT          NULL COMMENT '用户类型（0:平台用户，1:终端用户）',
    uid           VARCHAR(255) NULL COMMENT '用户账号',
    use_platforms VARCHAR(255) NULL COMMENT '用户使用的平台',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='用户信息表，存储用户的基本信息、联系方式、权限、角色等';


-- 文件名称: virtual_device.sql
-- 文件描述: 该SQL文件用于创建虚拟设备表 virtual_device。
--         该表用于存储虚拟设备的基本信息，包括虚拟设备名称、状态、行为脚本及触发方式等。
-- 使用场景: 适用于虚拟设备管理系统，记录虚拟设备的行为、状态、触发机制等信息。

CREATE TABLE virtual_device
(
    id                 VARCHAR(255) NOT NULL COMMENT '主键ID，唯一标识每个虚拟设备',
    create_by          BIGINT       NULL COMMENT '创建者，记录创建该虚拟设备的用户ID',
    create_dept        BIGINT       NULL COMMENT '创建部门，记录创建该虚拟设备的部门ID',
    create_time        DATETIME     NULL COMMENT '创建时间，记录虚拟设备创建的时间',
    update_by          BIGINT       NULL COMMENT '更新者，记录更新该虚拟设备的用户ID',
    update_time        DATETIME     NULL COMMENT '更新时间，记录虚拟设备最后一次更新的时间',
    create_at          BIGINT       NULL COMMENT '创建时间（Unix时间戳）',
    name               VARCHAR(255) NULL COMMENT '虚拟设备名称',
    product_key        VARCHAR(255) NULL COMMENT '产品key，标识该虚拟设备所属的产品',
    script             TEXT         NULL COMMENT '设备行为脚本，用于描述虚拟设备的行为',
    state              VARCHAR(255) NULL COMMENT '虚拟设备的运行状态',
    tenant_id          BIGINT       NULL COMMENT '租户编号，标识该虚拟设备所属的租户',
    `trigger`          VARCHAR(255) NULL COMMENT '触发方式，描述设备行为的执行方式',
    trigger_expression VARCHAR(255) NULL COMMENT '触发表达式，用于描述触发条件',
    type               VARCHAR(255) NULL COMMENT '虚拟设备的类型',
    uid                VARCHAR(255) NULL COMMENT '所属用户ID，标识虚拟设备属于哪个用户',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='虚拟设备表，存储虚拟设备的基本信息、行为脚本、状态、触发机制等';


-- 文件名称: virtual_device_mapping.sql
-- 文件描述: 该SQL文件用于创建虚拟设备映射表 virtual_device_mapping。
--         该表用于记录虚拟设备与租户之间的映射关系。
-- 使用场景: 适用于虚拟设备与实际设备的关联管理，帮助映射虚拟设备与对应的物理设备。

CREATE TABLE virtual_device_mapping
(
    id          VARCHAR(255) NOT NULL COMMENT '主键ID，唯一标识每个映射关系',
    create_by   BIGINT       NULL COMMENT '创建者，记录创建该映射关系的用户ID',
    create_dept BIGINT       NULL COMMENT '创建部门，记录创建该映射关系的部门ID',
    create_time DATETIME     NULL COMMENT '创建时间，记录虚拟设备映射创建的时间',
    update_by   BIGINT       NULL COMMENT '更新者，记录更新该映射关系的用户ID',
    update_time DATETIME     NULL COMMENT '更新时间，记录虚拟设备映射最后一次更新的时间',
    device_id   VARCHAR(255) NULL COMMENT '设备ID，标识物理设备的唯一标识',
    tenant_id   BIGINT       NULL COMMENT '租户编号，标识该映射关系所属的租户',
    virtual_id  VARCHAR(255) NULL COMMENT '虚拟设备ID，标识虚拟设备的唯一标识',
    CONSTRAINT `PRIMARY`
        PRIMARY KEY (id)
) COMMENT='虚拟设备与物理设备的映射表，记录虚拟设备与实际设备之间的关联关系';



