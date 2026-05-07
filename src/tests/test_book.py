books_prefix = "/api/v1/books"


def test_get_all_books(fake_session, fake_book_service, fake_client):
    response = fake_client.get(url=f"{books_prefix}")
    assert fake_book_service.get_all_books_called_once()
    assert fake_book_service.get_all_books_called_once_with(fake_session)
