# Generated by Django 4.2.11 on 2024-05-08 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Correspondence",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("corr_no", models.CharField(max_length=255)),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("high", "High"),
                            ("medium", "Medium"),
                            ("low", "Low"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "int_ext",
                    models.CharField(
                        choices=[("internal", "Internal"), ("external", "External")],
                        max_length=10,
                    ),
                ),
                ("name_of_designation", models.CharField(max_length=255)),
                ("email_id", models.EmailField(max_length=254)),
                ("type_of_doc", models.CharField(max_length=255)),
                ("do_received_from", models.CharField(max_length=255)),
                ("reference_number", models.CharField(max_length=100)),
                ("reference_date", models.DateField()),
                ("subject", models.CharField(max_length=255)),
                ("action_marked", models.CharField(max_length=255)),
                ("date_of_forwarding", models.DateField()),
                ("documents", models.CharField(max_length=255)),
                ("status", models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("slug_name", models.CharField(max_length=255)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("role_name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
                ("status", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="SubDepartment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("slug_name", models.CharField(max_length=255)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254, null=True, unique=True)),
                ("password", models.CharField(max_length=128)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserRoleMap",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="fts_app.role"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="fts_app.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, null=True, unique=True)),
                ("full_name", models.CharField(max_length=255)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fts_app.department",
                    ),
                ),
                (
                    "sub_department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fts_app.subdepartment",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="fts_app.user"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="subdepartment",
            name="created_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="fts_app.user"
            ),
        ),
        migrations.AddField(
            model_name="subdepartment",
            name="department_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sub_departments",
                to="fts_app.department",
            ),
        ),
        migrations.CreateModel(
            name="StoreDocument",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("filename", models.CharField(max_length=255)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("status", models.PositiveSmallIntegerField(default=1)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="fts_app.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("from_email", models.EmailField(max_length=254, null=True)),
                ("to_email", models.EmailField(max_length=254, null=True)),
                ("message", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
                (
                    "document",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="fts_app.storedocument",
                    ),
                ),
                (
                    "from_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_messages",
                        to="fts_app.user",
                    ),
                ),
                (
                    "to_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_messages",
                        to="fts_app.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DepartmentRoleMap",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="department_departmentrolemaps",
                        to="fts_app.department",
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="fts_app.role"
                    ),
                ),
                (
                    "sub_department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subdepartment_departmentrolemaps",
                        to="fts_app.subdepartment",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="department",
            name="created_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="fts_app.user"
            ),
        ),
        migrations.CreateModel(
            name="CorrespondenceUserMap",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("status", models.IntegerField(default=1)),
                (
                    "correspondence",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="correspondence_mappings",
                        to="fts_app.correspondence",
                    ),
                ),
                (
                    "from_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_correspondences",
                        to="fts_app.user",
                    ),
                ),
                (
                    "to_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_correspondences",
                        to="fts_app.user",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="correspondence",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fk_department",
                to="fts_app.department",
            ),
        ),
        migrations.AddField(
            model_name="correspondence",
            name="role",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="fts_app.role"
            ),
        ),
        migrations.AddField(
            model_name="correspondence",
            name="sub_department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fk_sub_department",
                to="fts_app.subdepartment",
            ),
        ),
        migrations.AddField(
            model_name="correspondence",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fk_user",
                to="fts_app.user",
            ),
        ),
    ]