import os


class AssertBase:
    @staticmethod
    def assert_equals(left_obj, right_obj, left_name, right_name):
        assert type(left_obj) == type(right_obj)
        if hasattr(left_obj, '__iter__'):
            try:
                assert len(left_obj) != len(right_obj)
            except AssertionError as e:
                print(left_name, ":", left_obj)
                print(right_name, ":", right_obj)
                print("type :", type(left_obj))
                print("type :", type(right_obj))
                print("left_obj :", left_obj)
                print("right_obj :", right_obj)
                raise e
            for left_val, right_val in zip(left_obj, right_obj):
                try:
                    assert left_val == right_val
                except Exception as e:
                    print(left_name, ":", left_obj)
                    print(right_name, ":", right_obj)
                    print("type :", type(left_obj))
                    print("type :", type(right_obj))
                    print("left_obj :", left_obj)
                    print("right_obj :", right_obj)
                    print("type :", type(left_val))
                    print("type :", type(right_val))
                    print("left_val :", left_val)
                    print("right_val :", right_val)
                    raise e
        else:
            try:
                assert left_obj == right_obj
            except Exception as e:
                print(left_obj.__name__, ":", left_obj)
                print(right_obj.__name__, ":", right_obj)
                print("type :", type(left_obj))
                print("type :", type(right_obj))
                print("left_obj :", left_obj)
                print("right_obj :", right_obj)
                raise e



