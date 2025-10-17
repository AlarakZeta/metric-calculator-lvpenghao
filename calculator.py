class MetricCalculator:
    def __init__(self):
        self.results = []
    
def calculate_mean(self, data):
        # data必须为列表或元组
        if not isinstance(data, (list, tuple)):
            raise TypeError("data必须为列表或元组")
        if len(data) == 0:
            return 0.0
        # 元素必须为数值
        for x in data:
            if not isinstance(x, (int, float)):
                raise ValueError("元素必须为数值")
        return sum(data) / len(data)

    def calculate_accuracy(self, y_true, y_pred):
        # y_true和y_pred必须为列表或元组
        if not isinstance(y_true, (list, tuple)) or not isinstance(y_pred, (list, tuple)):
            raise TypeError("y_true和y_pred必须为列表或元组")
        if len(y_true) == 0 or len(y_pred) == 0:
            return 0.0
        # 长度需一致
        if len(y_true) != len(y_pred):
            raise ValueError("y_true和y_pred长度必须一致")

        correct = 0
        for t, p in zip(y_true, y_pred):
            if t == p:
                correct += 1

        # 防止除零
        return correct / len(y_true) if len(y_true) > 0 else 0.0

    def add_metric(self, name, value):
        #name必须是字符串
        #value必须是数值
        if not isinstance(name, str):
            raise TypeError("name必须是字符串")
        if not isinstance(value, (int, float)):
            raise ValueError("value必须是数值")
        self.results.append((name, round(float(value), 4)))
    
    def get_results(self):
        return self.results
