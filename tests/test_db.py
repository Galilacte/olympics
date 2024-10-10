from olympics import db


def test_countries():
    rows = db.get_countries()
    assert len(rows) > 100
    
def test_countries2():
    rows = db.get_countries(2)
    assert len(rows) > 0
    
    

    
    
    
    
    
def test_athletes():
    rows = db.get_athletes()
    assert len(rows) > 100
    
    
def test_athletes2():
    rows = db.get_athletes(2)
    assert len(rows) > 0
    
    
def test_disciplines():
    rows = db.get_disciplines()
    assert len(rows) > 40
    
    
def test_disciplines2():
    rows = db.get_disciplines(2)
    assert len(rows) > 0
    
    
def test_teams():
    rows = db.get_teams()
    assert len(rows) > 10
    
    
    
def test_teams2():
    rows = db.get_teams(2)
    assert len(rows) > 0
    
    
    
def test_events():
    rows = db.get_events()
    assert len(rows) > 10
    
    
    
def test_events2():
    rows = db.get_events(2)
    assert len(rows) > 0
    
    
def test_medals():
    rows = db.get_medals()
    assert len(rows) > 10
    
    
def test_medals2():
    rows = db.get_medals(2)
    assert len(rows) > 0
    
    
def test_discipline_athletes():
    rows = db.get_discipline_athletes(1)
    assert len(rows) > 10
    
def test_top_countries():
    rows = db.get_top_countries()
    assert len(rows) > 2

    
    
def test_collective_medals():
    rows = db.get_collective_medals()
    assert len(rows) > 10
    
def test_top_collective():
    rows = db.get_top_collective()
    assert len(rows) > 2
    
def test_individual_medals():
    rows = db.get_individual_medals()
    assert len(rows) > 10
    
    
    
def test_individual_medals2():
    rows = db.get_individual_medals(2)
    assert len(rows) > 0
    
    
def test_top_individual():
    rows = db.get_top_individual()
    assert len(rows) > 2