#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_config():
    return {  # OWASP Nettacker Default Configuration
        "language": "en",
        "verbose_level": 0,
        "show_version": False,
        "check_update": False,
        "log_in_file": "results.html",
        "graph_flag": "d3_tree_v1_graph",
        "help_menu_flag": False,
        "targets": None,
        "targets_list": None,
        "scan_method": None,
        "exclude_method": None,
        "users": None,
        "users_list": None,
        "passwds": None,
        "passwds_list": None,
        "ports": None,
        "timeout_sec": 3.0,
        "time_sleep": 0.0,
        "check_ranges": False,
        "check_subdomains": False,
        "thread_number": 100,
        "thread_number_host": 30,
        "socks_proxy": None,
        "retries": 3,
        "ping_flag": False,
        "methods_args": None,
        "method_args_list": False,
        "startup_check_for_update": False
    }
