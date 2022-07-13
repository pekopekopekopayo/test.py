test_1_sql = """WITH ranking (total, user_rank, user_id) AS
                (
                SELECT 
                sum(price), 
                rank() over (order by sum(price) desc),
                user_id	
                from item 
                group by user_id
                )
                SELECT total, user_rank FROM ranking
                where ranking.user_id = 125;"""



test_2_sql = """SELECT SUB.TOTAL, SUB.USER_RANK FROM user, 
                (
                SELECT 
                SUM(PRICE) AS TOTAL,
                user_id,
                rank() over (order by SUM(PRICE) DESC) as USER_RANK
                FROM item
                GROUP BY USER_ID
                ) AS SUB
                WHERE user.ID = 125 AND SUB.user_id = 125"""




