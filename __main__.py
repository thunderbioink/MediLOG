print('HELLO WORLD')
# "Check if venv is active"
# import sys

# def get_base_prefix():
#     """Get base/real prefix, or sys.prefix if there is none."""
#     return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

# def in_virtualenv():
#     if get_base_prefix() != sys.prefix:
#         in_venv = print("in venv")
#         return in_venv, "in venv"
#     if get_base_prefix() == sys.prefix:
#         not_in_venv = print("not in venv")
#         return  not_in_venv, "not in venv"
#     # assert ""