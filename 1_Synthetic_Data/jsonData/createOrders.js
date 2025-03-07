const customers = require("./customers.json");
const products = require("./products.json");
const carriers = [ "FedEx", "UPS", "USPS", "DHL" ];
const services = [ "Priority", "Standard", "Economy" ];
function rand(max)
{
    return Math.floor(Math.random() * Math.floor(max));
}
function generateTrackingNumber()
{
    let trackingNumber = "";
    for(let i = 0; i < 4; i++)
    {
        trackingNumber += rand(10);
    }
    trackingNumber += " ";
    for(let i = 0; i < 4; i++)
    {
        trackingNumber += rand(10);
    }
    trackingNumber += " ";
    for(let i = 0; i < 4; i++)
    {
        trackingNumber += rand(10);
    }
    return trackingNumber;
}
let orders = [];
for(let o = 0; o < 3; o++)
{
    let order = {
        meta: {
            schemaVersion: 1,
            documentVersion: 1,
            source: 1
        },
        contactInfo: {},
        address: {
            line1: "123 Mullica Hill Road",
            city: "Glassboro",
            state: "NJ",
            country: "United States",
            postalCode: "08028"
        },
        orderInfo: {
            date: "2025-03-07",
            total: 0
        },
        products: [],
        shipping: {
            carrier: "",
            service: "",
            trackingNumber: "",
            costToStore: 5.00
        }
    };
    order.contactInfo = customers[rand(customers.length)];
    const numberOfProducts = rand(10) + 1;
    for(let p = 0; p < numberOfProducts; p++)
    {
        const product = products[rand(products.length)];
        const quantity = rand(10) + 1;
        order.products.push({
            product: product.name,
            quantity: quantity
        });
        order.orderInfo.total += product.price * quantity;
    }
    order.shipping.carrier = carriers[rand(carriers.length)];
    order.shipping.service = services[rand(services.length)];
    order.shipping.trackingNumber = generateTrackingNumber();
    orders.push(order);
}
console.log(orders);
//console.log(JSON.stringify(orders));