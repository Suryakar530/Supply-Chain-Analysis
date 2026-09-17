
-------------STEP 1 — Overall data validation

SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT sku) AS unique_skus,
    COUNT(DISTINCT product_type) AS product_types,
    COUNT(DISTINCT supplier_name) AS suppliers,
    COUNT(DISTINCT location) AS locations,
    COUNT(DISTINCT shipping_carriers) AS shipping_carriers,
    COUNT(DISTINCT transportation_modes) AS transportation_modes
FROM supply_chain;

SELECT
    column_name,
    data_type
FROM information_schema.columns
WHERE table_name = 'supply_chain'
ORDER BY ordinal_position;

------------STEP 2: Overall Business KPIs

SELECT
    COUNT(*) AS total_records,
    SUM(number_of_products_sold) AS total_products_sold,
    ROUND(SUM(revenue_generated), 2) AS total_revenue,
    ROUND(AVG(price), 2) AS average_product_price,
    ROUND(AVG(revenue_generated), 2) AS average_revenue_per_record,
    ROUND(AVG(shipping_costs), 2) AS average_shipping_cost,
    ROUND(AVG(manufacturing_costs), 2) AS average_manufacturing_cost,
    ROUND(AVG(defect_rates), 2) AS average_defect_rate
FROM supply_chain;

------------STEP 3-Revenue & Sales by Product Type

SELECT
    product_type,
    COUNT(*) AS total_records,
    SUM(number_of_products_sold) AS total_units_sold,
    ROUND(SUM(revenue_generated), 2) AS total_revenue,
    ROUND(AVG(price), 2) AS average_price
FROM supply_chain
GROUP BY product_type
ORDER BY total_revenue DESC;

--3.1: Top 10 Products by Revenue
SELECT
    sku,
    product_type,
    number_of_products_sold,
    revenue_generated,
    price
FROM supply_chain
ORDER BY revenue_generated DESC
LIMIT 10;

---3.2 :Top 10 Products by Units Sold

SELECT
    sku,
    product_type,
    number_of_products_sold,
    revenue_generated,
    price
FROM supply_chain
ORDER BY number_of_products_sold DESC
LIMIT 10;


------------STEP 4 — Revenue & Cost Analysis

---4.1 — Revenue vs Total Costs

SELECT
    ROUND(SUM(revenue_generated), 2) AS total_revenue,
    ROUND(SUM(shipping_costs), 2) AS total_shipping_cost,
    ROUND(SUM(manufacturing_costs), 2) AS total_manufacturing_cost,
    ROUND(SUM(costs), 2) AS total_other_costs,
    ROUND(
        SUM(shipping_costs)
        + SUM(manufacturing_costs)
        + SUM(costs), 2
    ) AS total_cost,
    ROUND(
        SUM(revenue_generated)
        - (
            SUM(shipping_costs)
            + SUM(manufacturing_costs)
            + SUM(costs)
        ), 2
    ) AS estimated_profit
FROM supply_chain;

---4.2 — Profit Margin

SELECT
    ROUND(SUM(revenue_generated), 2) AS total_revenue,
    ROUND(
        SUM(shipping_costs)
        + SUM(manufacturing_costs)
        + SUM(costs), 2
    ) AS total_cost,
    ROUND(
        SUM(revenue_generated)
        - (
            SUM(shipping_costs)
            + SUM(manufacturing_costs)
            + SUM(costs)
        ), 2
    ) AS estimated_profit,
    ROUND(
        (
            SUM(revenue_generated)
            - (
                SUM(shipping_costs)
                + SUM(manufacturing_costs)
                + SUM(costs)
            )
        ) / SUM(revenue_generated) * 100,
        2
    ) AS estimated_profit_margin
FROM supply_chain;

---4.3 — Cost by Product Type

SELECT
    product_type,
    ROUND(SUM(revenue_generated), 2) AS total_revenue,
    ROUND(SUM(shipping_costs), 2) AS shipping_cost,
    ROUND(SUM(manufacturing_costs), 2) AS manufacturing_cost,
    ROUND(SUM(costs), 2) AS other_cost,
    ROUND(
        SUM(shipping_costs)
        + SUM(manufacturing_costs)
        + SUM(costs), 2
    ) AS total_cost,
    ROUND(
        SUM(revenue_generated)
        - (
            SUM(shipping_costs)
            + SUM(manufacturing_costs)
            + SUM(costs)
        ), 2
    ) AS estimated_profit
FROM supply_chain
GROUP BY product_type
ORDER BY estimated_profit DESC;

---4.4 — Cost Efficiency by Product Type

SELECT
    product_type,

    ROUND(SUM(revenue_generated), 2) AS total_revenue,

    ROUND(
        SUM(shipping_costs)
        + SUM(manufacturing_costs)
        + SUM(costs), 2
    ) AS total_cost,

    ROUND(
        SUM(revenue_generated)
        - (
            SUM(shipping_costs)
            + SUM(manufacturing_costs)
            + SUM(costs)
        ), 2
    ) AS estimated_profit,

    ROUND(
        (
            SUM(shipping_costs)
            + SUM(manufacturing_costs)
            + SUM(costs)
        )
        / SUM(revenue_generated) * 100,
        2
    ) AS cost_percentage,

    ROUND(
        (
            SUM(revenue_generated)
            - (
                SUM(shipping_costs)
                + SUM(manufacturing_costs)
                + SUM(costs)
            )
        )
        / SUM(revenue_generated) * 100,
        2
    ) AS profit_margin

FROM supply_chain
GROUP BY product_type
ORDER BY profit_margin DESC;

------------STEP 5 — Inventory & Availability Analysis

---5.1 — Inventory Overview

SELECT
    ROUND(AVG(stock_levels), 2) AS average_stock_level,
    MIN(stock_levels) AS minimum_stock_level,
    MAX(stock_levels) AS maximum_stock_level,
    SUM(stock_levels) AS total_stock,
    ROUND(AVG(availability), 2) AS average_availability
FROM supply_chain;

---5.2 — Inventory by Product Type

SELECT
    product_type,
    SUM(stock_levels) AS total_stock,
    ROUND(AVG(stock_levels), 2) AS average_stock,
    SUM(number_of_products_sold) AS total_units_sold,
    ROUND(AVG(availability), 2) AS average_availability
FROM supply_chain
GROUP BY product_type
ORDER BY total_stock DESC;

---5.3: Potential Stock Risk

SELECT
    sku,
    product_type,
    stock_levels,
    number_of_products_sold,
    availability,
    CASE
        WHEN stock_levels = 0 THEN 'Out of Stock'
        WHEN stock_levels < number_of_products_sold THEN 'High Stock Risk'
        WHEN stock_levels < (number_of_products_sold * 0.25) THEN 'Medium Stock Risk'
        ELSE 'Healthy Stock'
    END AS inventory_status
FROM supply_chain
ORDER BY
    CASE
        WHEN stock_levels = 0 THEN 1
        WHEN stock_levels < number_of_products_sold THEN 2
        WHEN stock_levels < (number_of_products_sold * 0.25) THEN 3
        ELSE 4
    END,
    stock_levels ASC;

------------STEP 6 — Shipping & Logistics Analysis

---6.1 — Shipping Carrier Performance

SELECT
    shipping_carriers,
    COUNT(*) AS total_shipments,
    ROUND(AVG(shipping_times), 2) AS avg_shipping_time,
    ROUND(AVG(shipping_costs), 2) AS avg_shipping_cost,
    ROUND(SUM(shipping_costs), 2) AS total_shipping_cost
FROM supply_chain
GROUP BY shipping_carriers
ORDER BY total_shipments DESC;

---6.2 — Transportation Mode Performance

SELECT
    transportation_modes,
    COUNT(*) AS total_shipments,
    ROUND(AVG(shipping_times), 2) AS avg_shipping_time,
    ROUND(AVG(shipping_costs), 2) AS avg_shipping_cost,
    ROUND(SUM(shipping_costs), 2) AS total_shipping_cost
FROM supply_chain
GROUP BY transportation_modes
ORDER BY avg_shipping_time ASC;

---6.3 — Shipping Cost by Product Type

SELECT
    product_type,
    ROUND(SUM(shipping_costs), 2) AS total_shipping_cost,
    ROUND(AVG(shipping_costs), 2) AS avg_shipping_cost,
    ROUND(AVG(shipping_times), 2) AS avg_shipping_time
FROM supply_chain
GROUP BY product_type
ORDER BY total_shipping_cost DESC;

---6.4 — Route Performance

SELECT
    routes,
    COUNT(*) AS total_shipments,
    ROUND(AVG(shipping_times), 2) AS avg_shipping_time,
    ROUND(AVG(shipping_costs), 2) AS avg_shipping_cost
FROM supply_chain
GROUP BY routes
ORDER BY avg_shipping_time ASC;

------------STEP 7 — Quality & Defect Analysis

---7.1 — Overall Quality Performance

SELECT
    COUNT(*) AS total_records,
    ROUND(AVG(defect_rates), 2) AS average_defect_rate,
    MIN(defect_rates) AS minimum_defect_rate,
    MAX(defect_rates) AS maximum_defect_rate,
    COUNT(*) FILTER (
        WHERE inspection_results = 'Pass'
    ) AS passed_inspections,
    COUNT(*) FILTER (
        WHERE inspection_results = 'Fail'
    ) AS failed_inspections
FROM supply_chain;

---7.2 — Quality by Product Type

SELECT
    product_type,
    COUNT(*) AS total_records,
    ROUND(AVG(defect_rates), 2) AS average_defect_rate,
    COUNT(*) FILTER (
        WHERE inspection_results = 'Pass'
    ) AS passed_inspections,
    COUNT(*) FILTER (
        WHERE inspection_results = 'Fail'
    ) AS failed_inspections,
    ROUND(AVG(manufacturing_costs), 2) AS avg_manufacturing_cost
FROM supply_chain
GROUP BY product_type
ORDER BY average_defect_rate DESC;

---7.3 — Highest-Defect Products

SELECT
    sku,
    product_type,
    ROUND(defect_rates, 2) AS defect_rate,
    inspection_results,
    manufacturing_costs
FROM supply_chain
ORDER BY defect_rates DESC
LIMIT 10;

---7.4 — Quality Risk Classification

SELECT
    sku,
    product_type,
    defect_rates,
    inspection_results,
    CASE
        WHEN defect_rates >= 3 THEN 'High Quality Risk'
        WHEN defect_rates >= 1.5 THEN 'Medium Quality Risk'
        ELSE 'Low Quality Risk'
    END AS quality_risk
FROM supply_chain
ORDER BY defect_rates DESC;

------------Step 8-Final Business Insights

---Step 8.1 — Executive Business Summary

SELECT
    COUNT(*) AS total_records,
    SUM(number_of_products_sold) AS total_units_sold,

    ROUND(SUM(revenue_generated), 2) AS total_revenue,

    ROUND(
        SUM(shipping_costs)
        + SUM(manufacturing_costs)
        + SUM(costs), 2
    ) AS total_cost,

    ROUND(
        SUM(revenue_generated)
        -
        (
            SUM(shipping_costs)
            + SUM(manufacturing_costs)
            + SUM(costs)
        ), 2
    ) AS estimated_profit,

    ROUND(
        (
            SUM(revenue_generated)
            -
            (
                SUM(shipping_costs)
                + SUM(manufacturing_costs)
                + SUM(costs)
            )
        ) / SUM(revenue_generated) * 100,
        2
    ) AS estimated_profit_margin,

    ROUND(AVG(stock_levels), 2) AS average_stock_level,

    ROUND(AVG(availability), 2) AS average_availability,

    ROUND(AVG(shipping_times), 2) AS average_shipping_time,

    ROUND(AVG(defect_rates), 2) AS average_defect_rate

FROM supply_chain;
