from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("pypi:pybuilder_docker")


name = "{{cookiecutter.project_slug}}"
default_task = "publish"


@init
def initialize(project):
    build_number = project.get_property("build_number")
    if build_number is not None and "" != build_number:
        project.version = build_number
    else:
        project.version = "0.0.999"

    #Project Manifest
    project.depends_on_requirements("src/main/python/requirements.txt")
    project.set_property('unittest_module_glob', 'test_*')
    project.set_property('coverage_branch_threshold_warn', 40)
    project.set_property('coverage_branch_partial_threshold_warn', 40)
    project.set_property('docker_package_build_img', '{{cookiecutter.application}}/{{cookiecutter.role}}:{}'.format(project.version))
    project.set_property('docker_push_img', '{{cookiecutter.application}}/{{cookiecutter.role}}')
    project.set_property('docker_push_registry', '{{cookiecutter.docker_registry}}')
    project.include_file('license-update', "config.json")

    project.summary = "{{cookiecutter.project_name}}"
    project.home_page = "{{cookiecutter.repository_url}}"
    project.description = "{{cookiecutter.description}}"
    project.author = "{{cookiecutter.owner}}"
    project.url = "{{cookiecutter.repository_url}}"

