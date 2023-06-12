# Question #2 (SQL)

**Given these two tables:**

Table: USA_CUSTOMERS (USA)

| ID  | NAME   |
| --- | ------ |
| 1   | Thomas |
| 3   | Cindy  |

Table: EU_CUSTOMERS (EU)

| ID  | NAME     |
| --- | -------- |
| 2   | Francois |
| 1   | Thomas   |

What would be the output of the following select statements?

| Select USA.NAME, EU.NAME From USA, EU Where USA.ID = EU.ID | Select USA.NAME, EU.NAME From USA left join EU on (USA.ID = EU.ID) | Select USA.NAME, EU.NAME From USA, EU |
| ---------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------- |
|                                                            |                                                                    |                                       |

For later discussion: we use those tables to keep track of our European and American customers. Please provide a critique to that table design (is it good? How could it be better?).

### Query 1:

| name   | name   |
| ------ | ------ |
| Thomas | Thomas |

This is inner join

### Query 2:

| name   | name   |
| ------ | ------ |
| Thomas | Thomas |
| Cindy  | null   |

EU.NAME in the second row is null because the name there are no row with ID = 3 in EU. In left join, the right side become null.

### Query 3:

| name   | name     |
| ------ | -------- |
| Thomas | Francois |
| Cindy  | Francois |
| Thomas | Thomas   |
| Cindy  | Thomas   |

This is cartesian product, every row on table a will once be paired with every row in table b.
