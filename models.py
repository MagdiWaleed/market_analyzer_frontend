class Product():
    def __init__(self, name, advantages, weaknesses):
        self.name = name
        self.advantages = advantages
        self.weaknesses = weaknesses

class Company():
    def __init__(self, products, overall_advantages, overal_weaknesses, name):
        self.name = name
        self.products = products
        self.overall_advantages = overall_advantages
        self.overal_weaknesses = overal_weaknesses

class FinalAnswer():
    def __init__(self,recommendations,gapInMarket):
        self.recommendations = recommendations
        self.gapInMarket = gapInMarket


class MarketDetails():

    def __init__ (self, data):
        if not isinstance(data, dict):
            data = self.toMap(data)
        self.marketType = data['marketIntent']['marketType']
        self.description = data['marketIntent']['description']
        self.product = data['marketIntent']['product']
        self.inhancedUserMessage = data['marketIntent']['inhancedUserMessage']
        self.companies = []
        for i, companyData in enumerate(data['companiesDetails']):
            products = []
            for productData in companyData['products']:
                product = Product(
                    name=productData['name'],
                    advantages=productData['advantages'],
                    weaknesses=productData['weaknesses']
                )
                products.append(product)
            company = Company(
                products=products,
                overall_advantages=companyData['overall_advantages'],
                overal_weaknesses=companyData['overal_weaknesses'],
                name=data['competitorCompanies'][i] if data['competitorCompanies'] else f"Company_{i+1}"
            )
            self.companies.append(company)
        self.finalAnswer = FinalAnswer(data['finalAnswer']['recommendations'],data['finalAnswer']['gapInMarket'])
    def toMap(self, result):
        new_data = {
            "marketIntent":{
                "marketType":result['marketIntent'].marketType,
                "description": result["marketIntent"].description,
                "product": result["marketIntent"].product,
                "inhancedUserMessage": result["marketIntent"].inhancedUserMessage
            },
            'competitorCompanies':[company.name for company in result['competitorCompanies'].competitorCompanies],
            "companiesDetails":[{
                
                    "overall_advantages":company.overall_advantages,
                    "overal_weaknesses":company.overal_weaknesses,
                    "products":[
                        {
                        "name":product.name,
                        "advantages":product.advantages,
                        "weaknesses":product.weaknesses
                        } for product in company.products]
                
                } for company in result['companiesDetails']
                ],
            "finalAnswer":{
                    "gapInMarket":result['finalAnswer'].gapInMarket,
                    "recommendations":result['finalAnswer'].recommendations
            }
        }
        return new_data
