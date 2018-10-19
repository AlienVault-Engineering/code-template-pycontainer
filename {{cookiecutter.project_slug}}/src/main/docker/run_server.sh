#!/usr/bin/env bash
cd /task
echo "Running from build ${BUILD_VERSION}"
{{cookiecutter.role}}
echo "Entry point done"
