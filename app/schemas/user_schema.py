from marshmallow import fields, Schema, validate, ValidationError


def validate_password(password):
    """验证密码强度"""
    if len(password) < 6:
        raise ValidationError("密码长度不能小于6位")

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True, validate=validate.Length(min=3, max=20))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate_password, load_only=True)