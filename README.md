# MLModel-Rest-API

The REST API is used for estimating the severity of a Covid-19 patient, on a scale of 100. Upon making a GET request on the `/api` endpoint, along with the necessary parameters, the Rest API returns a severity score of a Covid-19 patient, in JSON format.

Link for Machine Learning Model: [https://github.com/dhruva-shashi/MLModel-Regressor](https://github.com/dhruva-shashi/MLModel-Regressor)

## Deployment

The REST API is deployed on Heroku platform. It is written in Python and was built using a Bottle server.

Link: [https://covid-project-api.herokuapp.com/](https://covid-project-api.herokuapp.com/)

## Factors used for Analysis

- Age
- Gender
- Pre-existing comrobidities
- Pneumonia
- Pregnancy

## Pre-existing comorbidities used for analysis

- Diabetes
- Chronic obstructive pulmonary disease (COPD)
- Asthma
- Hypertension
- Cardiovascular diseases
- Kidney disorders
- Obesity
- Tobacco consumption
- Other diseases

## HTTP Request

To estimate the severity of a Covid-19 patient, we make a `GET` request to the `/api` endpoint

`GET /api`

## Query Parameters

The HTTP requests takes a single parameter, `param`, which is mandatory and is used for making estimations.

Following are the factors and the value type which must be passed via the `param` parameter. All the values must be comma separated and passed via `param`, in the same order in which it is given in the table.

| No | Factor | Type |
| --- | ------ | ---- |
| 1 | Pneuomnia | True/False (1/0) |
| 2 | Age | Non-negative Integer |
| 3 | Pregnancy | True/False (1/0) |
| 4 | Diabetes | True/False (1/0) |
| 5 | COPD | True/False (1/0) |
| 6 | Asthma | True/False (1/0) |
| 7 | Hypertension | True/False (1/0) |
| 8 | Other Diseases | True/False (1/0) |
| 9 | Cardiovascular Diseases | True/False (1/0) |
| 10 | Obesity | True/False (1/0) |
| 11 | Kidney Disorders | True/False (1/0) |
| 12 | Tobacco consumer | True/False (1/0) |
| 13 | Male | True/False (1/0) |
| 14 | Female | True/False (1/0) |
| 15 | Transgender | True/False (1/0) |

## Response

If successful, the message returns a `200 OK` response code and the estimation of the risk of the Covid-19 patient if the parameters were passed correctly.

## Example

The following example, makes a prediction of a male patient whose age is 80 years and who is suffering from diabetes and cardiovascular diseases

### Request

The values are passed to the `param`, parameters, according to the order given in the table. They values are comma separated.

`GET https://covid-project-api.herokuapp.com/api?param=0,80,0,1,0,0,0,0,1,0,0,0,1,0,0`

### Response

For the above request, the following response is returned

```
HTTP/1.1 200 OK
Content-type: application/json

{
    "ok": true, 
    "risk": 90.52910052910053
}
```

## Errors

If any error occurs while making predictions using the Machine Learning Model, the value of `ok` in the JSON response is set to `false` and a value for `error` is present in the JSON response.

Example for a response which returns an error:

```
HTTP/1.1 200 OK
Content-type: application/json

{
    "ok": false
    "error": "X has 14 features, but RandomForestRegressor is expecting 15 features as input."
}
```


