import pandas as pd


df = pd.read_csv('Dataset/CSV_EQUIPE_ADVERSE.csv')
colonnes_a_supprimer = [
    'own_goals', 'opponent_manager_name', 'hosting', 'opponent_position', 'opponent_id',
    'own_manager_name', 'url', 'filename', 'last_season', 'coach_name',
    'net_transfer_record', 'stadium_seats', 'stadium_name', 'national_team_players',
    'foreigners_percentage', 'foreigners_number', 'average_age', 'squad_size',
    'total_market_value', 'club_code', 'confederation', 'description',
    'player_in_id', 'player_assist_id', 'type', 'team_captain'
]


df = df.drop(columns=colonnes_a_supprimer)

df.to_csv('Dataset/CSV_EQUIPE_ADVERSE.csv', index=False)
