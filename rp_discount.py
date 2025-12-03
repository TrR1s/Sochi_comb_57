import numpy as np
from scipy import stats



def ev_discount(ev_session:float,std_session:float, discount:int, min_loss_for_discount=0 ) -> float:
    """Считает MO сессии с данными условиями дискаунта

    Args:
        ev_session (float): Теор. Мат. Ожидание сессии
        std_session (float): Теор. СКО сессии
        discount (int): Процент дискаунта (0.05  -  5%)
        min_loss_for_discount (int, optional): Минимальный результат игрока,
                                            после которого он получает дискаунт
                                            NB: значение должно быть с минусом (min_loss_for_discount = -10_000)
                                            . Defaults to 0.

    Returns:
        float: Теор. Мат. Ожидание с дискаунтом.
    """
    
    x = np.linspace(ev_session-4*std_session,ev_session+4*std_session,num=1_000)
    norm_gen = stats.norm(ev_session,std_session)
    x_i = [ (x[i-1]+x[i])/2  for i in range(1,len(x))]
    x_i = np.fromiter(map(lambda xi: xi if xi > min_loss_for_discount else xi + abs(xi)*discount,x_i), dtype=np.float64)
    p_i = np.fromiter([ (norm_gen.cdf(x[i]) - norm_gen.cdf(x[i-1])) for i in range(1,len(x))], dtype=np.float64)
    return (x_i*p_i).sum()

ev_session = -240
std_session  = 9000

discount = 0.05
min_loss_for_discount = -10000



import unittest

class TestMyMathFunctions(unittest.TestCase):
    def test_count_ev_discount(self):
        ev_session = -240
        std_session  = 9000

        discount = 0.05
        min_loss_for_discount = -10000
        result = ev_discount(ev_session,std_session,discount,min_loss_for_discount)
        self.assertAlmostEqual(result, -138.7, places=1)


if __name__ == '__main__':
    unittest.main()