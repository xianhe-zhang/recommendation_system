from recall.strategy.recall_strategy import RecallStrategy
from redis import Redis
from recall.dataset import embedding
from recall.model.lsh import get_item_lsh

class RecentClickStrategy(RecallStrategy):
    def __init__(self) -> None:
        super().__init__()
        self.redis = Redis()
        self.lsh = get_item_lsh()

    def name(self):
        return 'RecentClick'

    def recall(self, context, n=20):
        if context.user_id is None:
            return []

        user_id = context.user_id
        redis_key = f'recent_clicks:{user_id}'
        recent_clicks = self.redis.hgetall(redis_key)
        recent_click_anime_ids = [int(k.decode()) for k in recent_clicks.keys()]
        if len(recent_click_anime_ids) == 0:
            return []
        print(f'user {user_id} recent clicked animes: {recent_click_anime_ids}')

        recent_click_anime_ids = recent_click_anime_ids[:10]
        num = int(n / len(recent_click_anime_ids))
        similar_animes = [self.similar_animes_for(aid, num) for aid in recent_click_anime_ids]
        print('similar animes')
        print(similar_animes)

        return [id for l in similar_animes for id in l]

    def similar_animes_for(self, anime_id, n):
        anime_emb = embedding.get_one_item_embedding(anime_id)
        if anime_emb is None:
            return []

        print(f'anime {anime_id} emb is {anime_emb}')

        return [id for id in self.lsh.search(anime_emb, n=n) if id != anime_id]
    
