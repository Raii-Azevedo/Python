UNION ALL

SELECT 
    nrc.country_abv_cd AS country_code,
    nrc.period_cd AS reference_date,
    nrc.fcc_cd,
    prod.manufacturer_cd,
    prod.atc_iv_cd,
    3 AS source_type,
    'NRC' AS source_desc,
    nrc.units_qty AS units,

    CASE
        WHEN nrc.country_abv_cd IN ('BRA', 'ARG', 'COL', 'MEX') 
            THEN nrc.list_values_lc_amt / (1 / cr.info_er)
        ELSE nrc.list_values_usd_amt
    END AS dollars_not_discounted,

    nrc.list_values_lc_amt AS local_currency_not_discounted,

    CASE
        WHEN nrc.country_abv_cd = 'MEX' 
             AND nrc.channel_desc IN ('Hospital Privado', 'Aseguradora') 
            THEN nrc.list_values_lc_amt / (1 / cr.info_er)
        WHEN nrc.country_abv_cd = 'MEX' 
             AND nrc.disc_values_lc_amt = 0 
            THEN nrc.list_values_lc_amt / (1 / cr.info_er)
        WHEN nrc.country_abv_cd IN ('BRA', 'COL', 'MEX') 
            THEN nrc.disc_values_lc_amt / (1 / cr.info_er)
        WHEN nrc.country_abv_cd = 'ARG' 
            THEN nrc.list_values_lc_amt / (1 / cr.info_er)
        ELSE nrc.list_values_lc_amt
    END AS dollars_discounted,

    CASE
        WHEN nrc.country_abv_cd = 'MEX' 
             AND nrc.channel_desc IN ('Hospital Privado', 'Aseguradora') 
            THEN nrc.list_values_lc_amt
        WHEN nrc.country_abv_cd = 'MEX' 
             AND nrc.disc_values_lc_amt = 0 
            THEN nrc.list_values_lc_amt
        WHEN nrc.country_abv_cd IN ('BRA', 'COL', 'MEX') 
            THEN nrc.disc_values_lc_amt
        ELSE nrc.list_values_lc_amt
    END AS local_currency_discounted,

    nrc.channel_desc,
    nrc.ref_frz_dt

FROM trusted_processed.fct_latam_iqvia_marketdata_nrc_pharma_processed_frz AS nrc

INNER JOIN product AS prod 
    ON nrc.country_abv_cd = prod.country_abv_cd
   AND nrc.fcc_cd = prod.fcc_cd
   AND nrc.ref_frz_dt = prod.ref_frz_dt

LEFT JOIN exchange_info_er AS cr 
    ON nrc.country_abv_cd = cr.country

-- Filtering rules
WHERE nrc.country_abv_cd != 'MEX' 
      OR nrc.channel_desc NOT IN ('Other Channels')
  AND (
        (nrc.country_abv_cd = 'BRA' 
         AND nrc.ref_frz_dt = (
                SELECT field_value
                FROM self_service_ingestion.tbl_latam_sharepoint_latam_dna_data_reference_parameter
                WHERE context = 'RegionalMarketData_Brazil'
             )
        )
      );
