from bottle import post, request, response, static_file
import uuid
import os
import uuid
import magic
import x

@post("/api-upload-avatar")
def _():
    try:
        # image = request.forms.get("upload_profile_image")
        form_image = request.files.get("profile_image")
        print("test", form_image)

        name,ext = os.path.splitext(form_image.filename)
        print("#"*30)
        print(name)
        print(ext)

        if ext not in (".png", ".jpg", ".jpeg"):
            raise Exception (400, "file extension not allowed")

        # Save the uploaded file to a temporary location
        temp_filename = f"temporary location/{uuid.uuid4().hex}{ext}"
        form_image.save(temp_filename)
        print(temp_filename)

        mime = magic.Magic(mime=True)
        mime_check = mime.from_file(temp_filename)

        if mime_check in ("image/png", "image/jpg", "image/jpeg"):
            print("image", mime_check)
            image_id = str(uuid.uuid4().hex)
            image_name = image_id + ext
            print("img name", image_name)
            # form_image.save(f"images/avatar/{image_name}")
            permanent_location = f"images/avatar/{image_name}"
            os.rename(temp_filename, permanent_location)

            # get user from cookie
            user = request.get_cookie("user", secret="my-secret")
            user_email = user[0]['user_email']
            print(user_email)

            # Open the db and get user
            db = x.db()
            current_avatar_filename = db.execute("SELECT user_avatar FROM users WHERE user_email=?", (user_email,)).fetchone()['user_avatar']

            # Remove old avatar from images folder
            if current_avatar_filename:
                # Remove the old avatar image file
                old_avatar_path = f"images/avatar/{current_avatar_filename}"
                os.remove(old_avatar_path)

            # Update the user's avatar filename in the database
            db.execute("UPDATE users SET user_avatar=? WHERE user_email=?", (image_name, user_email))
            db.commit()

            return "Image uploaded successfully!"
        else:
            print("not an image", mime_check)
            os.remove(temp_filename)
            response.status = 400
            raise Exception("You are only allowed to upload jpg, jpeg or png as images")
            # create popup error telling which file types if allowed

        return {"info": "picture uploaded"}
    except Exception as ex:
        if 'db' in locals(): db.rollback()
        print(ex)
    finally:
        if 'db' in locals(): db.close()