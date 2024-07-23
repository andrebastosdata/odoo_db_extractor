class OdooConfig:
        yaml_path = '/Workspace/databricks_mb/0_bronze/odoo_db/configs/ingestion_datails.yaml'
        source  = 'odoo_prd.public'
        target  = 'bronze_mb_dev.odoo_prd'
        timezone_str = 'America/Sao_Paulo'
        column_date = 'write_date'
        column_key = 'id'

class IngestionInfo:
        tables = 'tables'
        table_name = 'table_name'
        source = 'source' 
        target = 'target'
        frequency = 'frequency'
        timezone_str = 'timezone_str'
        type_load = 'type_load'
        update_dl = 'update_dl'
        timezone_dl = 'timezone_dl'

class Tables:
        brm_book = 'brm_book'
        res_partner = 'res_partner'
        seeds_environment = 'seeds_environment'
        x_contrato_line_c280f = 'x_contrato_line_c280f'
        x_contrato = 'x_contrato'
