from models import db, Category, Author

if __name__ == '__main__':
    категорії = [
        Category(категорія='Фантастика'),
        Category(категорія='Детектив'),
        Category(категорія='Трилер'),
        Category(категорія='Комедія'),
        Category(категорія='Драма')
    ]

    автори = [
        Author(автор='Дж. К. Роулінг'),
        Author(автор='Стівен Кінг'),
        Author(автор='Дж. Р. Р. Толкін'),
        Author(автор='Агата Крісті'),
        Author(автор='Мігель де Сервантес')
    ]

    db.session.add_all(категорії)
    db.session.add_all(автори)
    db.session.commit()