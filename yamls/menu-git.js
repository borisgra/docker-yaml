
export function menuItemsData(newGreed)  {
    const defColor = {color: '#0033cc',bgcolor: '#c6ecc6'}
    const baseUrl = 'https://query-gra-hyx2izic7a-uc.a.run.app'
    // const baseUrlKoyeb = 'https://query-gra.koyeb.app'
    const baseUrlQuery = 'https://query-gra-hyx2izic7a-uc.a.run.app'
    const baseUrlDSV = 'https://dsv-hyx2izic7a-uc.a.run.app'
    return  {
        label: 'menu',
        items: [
            {
                label: 'Olympic winners  GIT !!',
                callback: (_, item) => newGreed("https://www.ag-grid.com/example-assets/olympic-winners.json", item.label),
                sx: defColor
            },
            {
                label: 'Clients query',
                callback: (_, item) => newGreed("https://query-gra-hyx2izic7a-uc.a.run.app/bd/supabase/jsonPG/public.v_persons/ and status <> 'client'", item.label),
                sx: defColor
            },
            {
                label: 'Clients dsv',
                callback: (_, item) => newGreed(`${baseUrlDSV}/bd/supabase/jsonPG/public.v_persons/ and status <> 'client'`, item.label),
                sx: defColor
            },
            {
                label: 'Soundproofing)',
                sx: defColor,
                delay: 300,
                items: [
                    {
                        label: 'Today (query)',
                        callback: (_, item) => newGreed(`${baseUrlQuery}/bd/daas_nma/jsonPG/v_history/ and  date(write_date)=current_date  order by id desc`, item.label),
                        sx: defColor
                    },
                    {
                        label: 'Month (query)',
                        callback: (_, item) => newGreed(`${baseUrlQuery}/bd/daas_nma/jsonPG/v_history/ and  date(write_date)>=cast(TO_CHAR(NOW(), 'yyyy-mm-01')as date) order by id desc`, item.label),
                        sx: defColor
                    },
                    {
                        label: 'Month (dsv)',
                        callback: (_, item) => newGreed(`${baseUrlDSV}/bd/daas_nma/jsonPG/v_history/ and  date(write_date)>=cast(TO_CHAR(NOW(), 'yyyy-mm-01')as date) order by id desc`, item.label),
                        sx: defColor
                    },
                    {
                        label: 'Today  (dsv)',
                        callback: (_, item) => newGreed(`${baseUrlDSV}/bd/daas_nma/jsonPG/v_history/ and  date(write_date)=current_date  order by id desc`, item.label),
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
                                callback: (_, item) => newGreed(`${baseUrlQuery}/bd/vpn-gra/jsonPG/bigquery-public-data.country_codes.country_codes`, item.label),
                                sx: defColor,
                                disabled: false,
                            },
                            {
                                label: 'Country codes start "A"',
                                callback: (_, item) => newGreed(`${baseUrlQuery}/bd/vpn-gra/jsonPG/bigquery-public-data.country_codes.country_codes / and starts_with(alpha_2_code,'A')`, item.label),
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