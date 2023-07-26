from django.db.models import signals
from django.dispatch import receiver

import logging
import os

from . import models


"""
https://techincent.com/how-to-delete-file-when-models-instance-is-delete-or-update-in-django/
"""


# @receiver(signals.pre_init, sender=models.Person)
# def person_pre_init(sender, *args, **kwargs):
#     pass
#     # print(f"""pre_init
#     # sender : {sender}
#     # """)
#     # print(args, kwargs)
#     # print()


# @receiver(signals.pre_save, sender=models.Person)
# def person_pre_save(
#     signal, sender, instance, raw, using, update_fields, *args, **kwargs
# ):
#     # print(f"""pre_save
#     # signal        : {signal}
#     # sender        : {sender}
#     # instance      : {instance}
#     # raw           : {raw}
#     # using         : {using}
#     # update_fields : {update_fields}
#     # """)
#     # print(vars(instance))
#     # print()
#     # print(args)
#     # print(kwargs)
#     # print()
#     try:
#         old_img = instance.__class__.objects.get(uuid=instance.uuid).image.path
#         try:
#             new_img = instance.image.path
#         except Exception as e:
#             new_img = None
#             logging.exception(e)
#         # print(old_img)
#         # print(new_img)
#         if new_img != old_img:
#             if os.path.exists(old_img):
#                 os.remove(old_img)
#                 print("  ->", old_img)
#                 print("->  ", new_img)
#     except Exception as e1:
#         logging.exception(e1)
#         pass


# @receiver(signals.post_delete, sender=models.Person)
# def person_post_delete(sender, instance, *args, **kwargs):
#     """Clean Old Image file"""
#     try:
#         logging.info("|>", instance.image)
#         instance.image.delete(save=False)
#     except Exception as e3:
#         logging.exception(e3)
#         pass


# @receiver(signals.pre_delete, sender=models.Person)
# def person_pre_delete(sender, instance, using, origin, *args, **kwargs):
#     # print(f"""pre_delete
#     # sender   : {sender}
#     # instance : {instance}
#     # using    : {using}
#     # origin   : {origin}""")
#     # print(args, kwargs)
#     # print()
#     pass
