// import {MenuItemData } from 'mui-nested-menu';
// @ts-ignore
// import React from "react";
// import {Image_help} from "./suplements";

// import {Image_help} from "../src/suplements";
// import React from "react";

// import {MenuItemData} from "mui-nested-menu";
// import {Image_help} from "../src/suplements";
// import React from "react";

export function menuItemsData(newGreed)  {
    const defColor = {color: '#0033cc',bgcolor: '#c6ecc6'}
    const baseUrl = 'https://dsv-hyx2izic7a-uc.a.run.app'
    const baseUrlKoyeb = 'https://query-gra.koyeb.app'
    const baseUrlQuery = 'https://query-gra-hyx2izic7a-uc.a.run.app'
    return  {
        label: 'menu',
        items: [
            {
                label: 'Help',
                // leftIcon: <Help />,
                // rightIcon: <Image_help/>,
                callback: () => window.open("html/help.html"),
                sx: {color: 'braun',bgcolor: '#c6ecc6'},
            },
            {
                label: 'Olympic winners',
                callback: (_, item) => newGreed("https://www.ag-grid.com/example-assets/olympic-winners.json", item.label),
                sx: defColor
            },
            {
                label: 'Clients',
                callback: (_, item) => newGreed(`${baseUrl}/bd/supabase/jsonPG/public.v_persons/ and status <> 'client'`, item.label),
                sx: defColor
            },
            {
                label: 'Clients 2',
                callback: (_, item) => newGreed(`${baseUrl}/bd/supabase/jsonPG/public.v_persons/ and status <> 'client'`, item.label),
                sx: defColor
            },
            {
                label: 'Soundproofing)',
                sx: defColor,
                delay: 300,
                items: [
                    {
                        label: 'Today  (dsv)',
                        callback: (_, item) => newGreed(`${baseUrl}/bd/daas_nma/jsonPG/v_history/ and  date(write_date)=current_date  order by id desc`, item.label),
                        sx: defColor
                    },
                    {
                        label: 'Today (query)',
                        callback: (_, item) => newGreed(`${baseUrlQuery}/bd/daas_nma/jsonPG/v_history/ and  date(write_date)=current_date  order by id desc`, item.label),
                        sx: defColor
                    },
                    {
                        label: 'Month (dsv)',
                        callback: (_, item) => newGreed(`${baseUrl}/bd/daas_nma/jsonPG/v_history/ and  date(write_date)>=cast(TO_CHAR(NOW(), 'yyyy-mm-01')as date) order by id desc`, item.label),
                        sx: defColor
                    },
                    {
                        label: 'Month (koeb)',
                        callback: (_, item) => newGreed(`${baseUrlKoyeb}/bd/daas_nma/jsonPG/v_history/ and  date(write_date)>=cast(TO_CHAR(NOW(), 'yyyy-mm-01')as date) order by id desc`, item.label),
                        sx: defColor
                    },
                    {
                        label: 'Year (working)',
                        callback: (_, item) => newGreed(`${baseUrl}/bd/daas_nma/jsonPG/v_users_working/   and  date(date_last)>=cast(TO_CHAR(NOW(), 'yyyy-01-01') as date) order by tests_count desc `, item.label),
                        sx: defColor,
                        disabled: false,
                    },
                ],
            },
            {
                label: 'Bigquery Google',
                sx: defColor,
                items: [
                    {
                        label: 'Country',
                        sx: defColor,
                        items: [
                            {
                                label: 'Country codes',
                                callback: (_, item) => newGreed(`${baseUrlKoyeb}/bd/vpn-gra/jsonPG/bigquery-public-data.country_codes.country_codes`, item.label),
                                sx: defColor,
                                disabled: false,
                            },
                            {
                                label: 'Country codes start "A"',
                                callback: (_, item) => newGreed(`${baseUrlKoyeb}/bd/vpn-gra/jsonPG/bigquery-public-data.country_codes.country_codes / and starts_with(alpha_2_code,'A')`, item.label),
                                sx: defColor,
                                disabled: false,
                            },
                        ],
                    },
                    {
                        label: 'Type 2',
                        callback: (event, item) => console.log('Export > FT2 clicked', event, item),
                        sx: defColor,
                        disabled: true,
                    },
                ],
            },
        ],
    }
}