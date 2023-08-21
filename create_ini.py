def generate_nginx_conf(output_path, project_path, project_name):
    # Nginx配置模板内容
    nginx_template = """
server {{
    listen 6604;
    #server_name your_server_ip;
    access_log  /usr/local/nginx/logs/uwsgi6100.log;
    error_log /usr/local/nginx/logs/uwsgi6100_error.log debug;

    location / {{
        include uwsgi_params;
        uwsgi_pass unix:{project_path}/{project_name}/{project_name}.sock;
    }}

    location /static/ {{
        alias {project_path}/{project_name}/static_assets/;
    }}
}}
"""
    content = nginx_template.format(
        project_path=project_path, project_name=project_name)

    with open(output_path, 'w') as output:
        output.write(content)


def generate_uwsgi_ini(output_path, project_path, project_name):
    # uwsgi配置模板内容
    uwsgi_template = """
[uwsgi]
project_path = {project_path}

module = {project_name}.wsgi:application
processes = 6
threads = 2
master = true
vacuum = true
socket = %(project_path)/{project_name}/{project_name}.sock
chmod-socket = 664
chdir = %(project_path)/
log-date = true
daemonize=%(project_path)/uwsgi.log
log-maxsize = 5000000
max-requests=100
buffer-size=65535
static-map = /static=%(project_path)/static_assets
procname-prefix = {project_name}
"""
    content = uwsgi_template.format(
        project_path=project_path, project_name=project_name)

    with open(output_path, 'w') as output:
        output.write(content)


if __name__ == "__main__":
    NGINX_OUTPUT_PATH = 'nginx_settlement_project.conf'
    UWSGI_OUTPUT_PATH = 'uwsgi_settlement_project.ini'
    PROJECT_PATH = '/home/pyapp/workspace/'
    PROJECT_NAME = 'settlement_project'

    generate_nginx_conf(NGINX_OUTPUT_PATH, PROJECT_PATH, PROJECT_NAME)
    generate_uwsgi_ini(UWSGI_OUTPUT_PATH, PROJECT_PATH, PROJECT_NAME)
