
def dwnld_data():

    from bs4 import BeautifulSoup
    import pprint

    import json

    import um_spec_sites.umw_mazowieckie as umw_mazowieckie
    import um_spec_sites.umw_dolnyslask as umw_dolnyslask
    import um_spec_sites.umw_lubelskie as umw_lubelskie 
    import um_spec_sites.umw_lodzkie as umw_lodzkie
    import um_spec_sites.umw_podlaskiego as umw_podlaskiego
    import um_spec_sites.umw_wielkopol as umw_wielkopol

    # gathering data from specific BIP websites 

    site_umw_mazow = umw_mazowieckie.print_umw_site()
    umw_maz_news_pg = umw_mazowieckie.umw_site_news(site_umw_mazow)
    umw_maz_news = umw_mazowieckie.site_news_all(umw_maz_news_pg)

    with open("umw_news_results/umw_maz_news.json", "w", encoding="UTF-8") as wynik_json:
        json.dump(umw_maz_news, wynik_json, ensure_ascii=False, indent=4)

    site_umw_dslask = umw_dolnyslask.print_umw_site()
    umw_dslask_news_pg = umw_dolnyslask.umw_site_news(site_umw_dslask)
    umw_dslask_news = umw_dolnyslask.site_news_all(umw_dslask_news_pg)

    with open("umw_news_results/umw_dslask_news.json", "w", encoding="UTF-8") as wynik_json:
        json.dump(umw_dslask_news, wynik_json, ensure_ascii=False, indent=4)

    site_umw_lubel = umw_lubelskie.print_umw_site()
    umw_lubel_news_pg = umw_lubelskie.umw_site_news(site_umw_lubel)
    umw_lubel_news = umw_lubelskie.site_news_all(umw_lubel_news_pg)

    with open("umw_news_results/umw_lubel_news.json", "w", encoding="UTF-8") as wynik_json:
        json.dump(umw_lubel_news, wynik_json, ensure_ascii=False, indent=4)

    site_umw_lodz = umw_lodzkie.print_umw_site()
    umw_lodz_news_pg = umw_lodzkie.umw_site_news(site_umw_lodz)
    umw_lodz_news = umw_lodzkie.site_news_all(umw_lodz_news_pg)

    with open("umw_news_results/umw_lodz_news.json", "w", encoding="UTF-8") as wynik_json:
        json.dump(umw_lodz_news, wynik_json, ensure_ascii=False, indent=4)

    site_umw_podlas = umw_podlaskiego.print_umw_site()
    umw_podlas_news = umw_podlaskiego.site_news_all(site_umw_podlas)

    with open("umw_news_results/umw_podlas_news.json", "w", encoding="UTF-8") as wynik_json:
        json.dump(umw_podlas_news, wynik_json, ensure_ascii=False, indent=4)

    site_umw_wielkopol = umw_wielkopol.print_umw_site()
    umw_wielkopol_news_pg = umw_wielkopol.umw_site_news(site_umw_wielkopol)
    umw_wielkopol_news = umw_wielkopol.site_news_all(umw_wielkopol_news_pg)

    with open("umw_news_results/umw_wielkopol_news.json", "w", encoding="UTF-8") as wynik_json:
        json.dump(umw_wielkopol_news, wynik_json, ensure_ascii=False, indent=4)

    # After gathering raw material, last couple records from each json file are deleted due incoherent or deprecated format. 
    # Curated sets are saved in umw_news_results_curated directory.