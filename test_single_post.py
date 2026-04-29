def test_post_id(single_post):
   assert single_post["id"] == 1

def test_post_has_title(single_post):
   assert "title" in single_post

def test_post_has_body(single_post):
    assert "body" in single_post

def test_post_user_id(single_post):
   assert single_post["userId"] == 1