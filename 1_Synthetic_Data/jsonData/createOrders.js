/* 
    This value is used to control the number of orders.
    If we need more data to query against, we can simply
        increase this number.
*/
const CONFIG = {
    NUM_ORDERS : 100,
    QUANTITIES : [1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 5, 8],
    SERVICE_SELECTION : [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2]
}

const customers = require("./customers.json");
const products = require("./products.json");

const carriers = [ "FedEx", "UPS", "USPS", "DHL" ];
const services = [ ["Economy", 5.00], ["Standard", 12.50], ["Priority", 35.50] ];

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
for(let o = 0; o < CONFIG.NUM_ORDERS; o++)
{
    let order = {
        meta: {
            schema_version: 1,
            document_version: 1,
            source_comment: "Typical Order Placed By Customer"
        },

        contactInfo: {

        },

        address: {
            line_1: "123 Mullica Hill Road",
            city: "Glassboro",
            state: "NJ",
            country: "United States",
            postal_code: "08028"
        },

        order_info: {
            date: "2025-03-07",
            total: 0
        },

        products: [],

        shipping: {
            carrier: "",
            service: "",
            tracking_number: "",
            cost_to_store: 0.00
        }
    };
    
    order.contactInfo = customers[rand(customers.length)];
    const numberOfProducts = rand(10) + 1;
    for(let p = 0; p < numberOfProducts; p++)
    {
        const product = products[rand(products.length)];
        const quantity = CONFIG.QUANTITIES[rand(CONFIG.QUANTITIES.length)];
        order.products.push({
            product: product.name,
            item_total : product.price,
            quantity: quantity
        });
        order.order_info.total += product.price * quantity;
    }

    order.shipping.carrier = carriers[rand(carriers.length)];

    services_index = CONFIG.SERVICE_SELECTION[rand(CONFIG.SERVICE_SELECTION.length)]

    order.shipping.service = services[services_index][0];
    order.shipping.cost_to_store = services[services_index][1];
    order.shipping.tracking_number = generateTrackingNumber();
    orders.push(order);
}
//console.log(orders);
console.log(JSON.stringify(orders, null, 4));