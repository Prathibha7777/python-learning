def test_user_id(user_data):
    assert user_data["id"] == 1

def test_user_email(user_data):
    assert "email" in user_data

def test_total_users(all_users):
    assert len(all_users) == 10

def test_base_url_used(base_url):
    assert "jsonplaceholder" in base_url