from sklearn.metrics import classification_report, precision_score, recall_score
import joblib
import sys

def main(path_model, path_eval_data):
    model = joblib.load(path_model)
    data = pd.read_csv(path_eval_data)

    print(datos['label'], model.predict(datos['data']))
    print(precision_score(datos['label'], modelo.predict(datos['data'])))


if __name__ == '__main__':
    path_model, path_data = sys.argv[1], sys.argv[2]
    main(path_model, path_data)
