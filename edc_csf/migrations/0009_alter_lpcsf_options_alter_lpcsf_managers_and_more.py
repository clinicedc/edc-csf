# Generated by Django 4.2.5 on 2023-09-25 15:43

import _socket
from django.db import migrations, models
import django_audit_fields.fields.hostname_modification_field
import edc_sites.model_mixins
import edc_visit_tracking.managers


class Migration(migrations.Migration):
    dependencies = [
        ("edc_csf", "0008_alter_historicallpcsf_csf_amount_removed_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="lpcsf",
            options={
                "default_manager_name": "objects",
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Lumbar Puncture/Cerebrospinal Fluid",
                "verbose_name_plural": "Lumbar Puncture/Cerebrospinal Fluid",
            },
        ),
        migrations.AlterModelManagers(
            name="lpcsf",
            managers=[
                ("objects", edc_visit_tracking.managers.CrfModelManager()),
                ("on_site", edc_sites.model_mixins.CurrentSiteManager()),
            ],
        ),
        migrations.AlterField(
            model_name="historicallpcsf",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="historicallpcsf",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="historicallpcsf",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="historicallpcsf",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
        migrations.AlterField(
            model_name="lpcsf",
            name="device_created",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device created"),
        ),
        migrations.AlterField(
            model_name="lpcsf",
            name="device_modified",
            field=models.CharField(blank=True, max_length=10, verbose_name="Device modified"),
        ),
        migrations.AlterField(
            model_name="lpcsf",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default=_socket.gethostname,
                help_text="System field. (modified on create only)",
                max_length=60,
                verbose_name="Hostname created",
            ),
        ),
        migrations.AlterField(
            model_name="lpcsf",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
                verbose_name="Hostname modified",
            ),
        ),
    ]