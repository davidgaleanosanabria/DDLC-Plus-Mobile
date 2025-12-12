init python:
    import datetime

    class PlusCreditsEntry:
        def __init__(self, data: dict, id: str) -> None:
            self.id = id
            self.title = data['title']
            self.name = data['name']

    def parse_plus_credits_entries():
        import tomllib
        credits = {}
        with renpy.file("pluscredits_data.toml", False) as f:
            credits_toml_dict = tomllib.load(f)
            for entry_id, data in credits_toml_dict.items():
                credits[entry_id] = PlusCreditsEntry(data, entry_id)
        
        
        
        
        
        
        
        
        return credits

define plus_credits = parse_plus_credits_entries()


image pluscredits_cg1:
    "images/side_stories/credits/bgsayori.png"
    size (config.screen_width, config.screen_height)
    xanchor 0.25
image pluscredits_cg2:
    "images/side_stories/credits/bgnatsuki.png"
    size (config.screen_width, config.screen_height)
    xanchor 0.23
image pluscredits_cg3:
    "images/side_stories/credits/bgyuri.png"
    size (config.screen_width, config.screen_height)
    xanchor 0.22
image pluscredits_cg4:
    "images/side_stories/credits/bgmonika.png"
    size (config.screen_width, config.screen_height)
    xanchor 0.18
image pluscredits_cg5:
    "images/side_stories/credits/sm.png"
    size (config.screen_width, config.screen_height)
    xanchor 0.02
image pluscredits_cg6:
    "images/side_stories/credits/sy.png"
    size (config.screen_width, config.screen_height)
    xanchor 0.05
image pluscredits_cg7:
    "images/side_stories/credits/nm.png"
    size (config.screen_width, config.screen_height)
    xanchor 0.15
image pluscredits_cg8:
    "images/side_stories/credits/nm.png"
    size (config.screen_width, config.screen_height)
    xanchor -0.30
image pluscredits_cg9:
    "images/side_stories/credits/sn.png"
    size (config.screen_width, config.screen_height)
    xanchor 0.18
image pluscredits_cg10:
    "images/side_stories/credits/sn.png"
    size (config.screen_width, config.screen_height)
    xanchor -0.22
image pluscredits_cg11:
    "images/side_stories/credits/ym.png"
    size (config.screen_width, config.screen_height)
    xanchor 0.03
image pluscredits_cg12:
    "images/side_stories/credits/ny.png"
    size (config.screen_width, config.screen_height)
    xanchor -0.02


image pluscredits_ts_img:
    "images/side_stories/credits/teamSalvatoLogo.png"
    xalign 0.5 yalign 0.6
    zoom 0.5 subpixel True

image pluscredits_sf_img:
    "images/side_stories/credits/sf_logotype_color.png"
    xalign 0.5 yalign 0.5
    zoom 0.5 subpixel True

image pluscredits_sf_movie:
    Movie(play="images/side_stories/credits/SF_animated_logo.webm", loop=False)
    xalign 0.5 yalign 0.5
    zoom 0.4

image pluscredits_epilogue:
    "images/side_stories/credits/epilogue.png"
    size (config.screen_width, config.screen_height)
    xalign 0.5 yalign 0.5
    subpixel True
    zoom 1.1 alpha 0
    parallel:
        easein_cubic 4 zoom 1.00
    parallel:
        easeout 4 alpha 1

image plusgrad1 = "gui/grad1.png"


image pluscredits_game_title_t = AlphaMask("plusgrad1", Text(plus_credits['game_title'].title, style="pluscredits_title_large", xalign=0.5, yalign=0.4))
image pluscredits_game_title_n = AlphaMask("plusgrad1", Text(plus_credits['game_title'].name, style="pluscredits_name", xalign=0.5, yalign=0.5))

image pluscredits_written_and_directed_t = AlphaMask("plusgrad1", Text(plus_credits['written_and_directed'].title, style="pluscredits_title", xalign=0.5, yalign=0.4, size=28, outlines=[]))
image pluscredits_written_and_directed_n = AlphaMask("plusgrad1", Text(plus_credits['written_and_directed'].name, style="pluscredits_name", xalign=0.5, yalign=0.5, size=64, outlines=[]))

image pluscredits_TS_development_title_t = AlphaMask("plusgrad1", Text(plus_credits['TS_development_title'].title, style="pluscredits_title_u", xalign=0.5, yalign=0.4))
image pluscredits_TS_development_title_n = AlphaMask("plusgrad1", Text(plus_credits['TS_development_title'].name, style="pluscredits_name", xalign=0.5, yalign=0.5))
image pluscredits_TS_development_art_1_t = AlphaMask("plusgrad1", Text(plus_credits['TS_development_art_1'].title, style="pluscredits_title", xalign=0.5, yalign=0.4))
image pluscredits_TS_development_art_1_n = AlphaMask("plusgrad1", Text(plus_credits['TS_development_art_1'].name, style="pluscredits_name", xalign=0.5, yalign=0.5))
image pluscredits_TS_development_art_2_t = AlphaMask("plusgrad1", Text(plus_credits['TS_development_art_2'].title, style="pluscredits_title", xalign=0.5, yalign=0.4))
image pluscredits_TS_development_art_2_n = AlphaMask("plusgrad1", Text(plus_credits['TS_development_art_2'].name, style="pluscredits_name", xalign=0.5, yalign=0.5))
image pluscredits_TS_development_art_3_t = AlphaMask("plusgrad1", Text(plus_credits['TS_development_art_3'].title, style="pluscredits_title", xalign=0.5, yalign=0.4))
image pluscredits_TS_development_art_3_n = AlphaMask("plusgrad1", Text(plus_credits['TS_development_art_3'].name, style="pluscredits_name", xalign=0.5, yalign=0.5))

image pluscredits_TS_development_programming_t = AlphaMask("plusgrad1", Text(plus_credits['TS_development_programming'].title, style="pluscredits_title", xalign=0.5, yalign=0.4))
image pluscredits_TS_development_programming_n = AlphaMask("plusgrad1", Text(plus_credits['TS_development_programming'].name, style="pluscredits_name", xalign=0.5, yalign=0.5))
image pluscredits_TS_development_UI_design_t = AlphaMask("plusgrad1", Text(plus_credits['TS_development_UI_design'].title, style="pluscredits_title", xalign=0.5, yalign=0.4))
image pluscredits_TS_development_UI_design_n = AlphaMask("plusgrad1", Text(plus_credits['TS_development_UI_design'].name, style="pluscredits_name", xalign=0.5, yalign=0.5))
image pluscredits_TS_development_music_1_t = AlphaMask("plusgrad1", Text(plus_credits['TS_development_music_1'].title, style="pluscredits_title", xalign=0.5, yalign=0.4))
image pluscredits_TS_development_music_1_n = AlphaMask("plusgrad1", Text(plus_credits['TS_development_music_1'].name, style="pluscredits_name", xalign=0.5, yalign=0.5))
image pluscredits_TS_development_music_2_t = AlphaMask("plusgrad1", Text(plus_credits['TS_development_music_2'].title, style="pluscredits_title", xalign=0.5, yalign=0.4))
image pluscredits_TS_development_music_2_n = AlphaMask("plusgrad1", Text(plus_credits['TS_development_music_2'].name, style="pluscredits_name", xalign=0.5, yalign=0.5))
image pluscredits_TS_development_music_3_t = AlphaMask("plusgrad1", Text(plus_credits['TS_development_music_3'].title, style="pluscredits_title", xalign=0.5, yalign=0.4))
image pluscredits_TS_development_music_3_n = AlphaMask("plusgrad1", Text(plus_credits['TS_development_music_3'].name, style="pluscredits_name", xalign=0.5, yalign=0.5))

image pluscredits_TS_production_title_t = AlphaMask("plusgrad1", Text(plus_credits['TS_production_title'].title, style="pluscredits_title_u", xalign=0.5, yalign=0.4))
image pluscredits_TS_production_title_n = AlphaMask("plusgrad1", Text(plus_credits['TS_production_title'].name, style="pluscredits_title_u", xalign=0.5, yalign=0.5))
image pluscredits_TS_production_creative_director_t = AlphaMask("plusgrad1", Text(plus_credits['TS_production_creative_director'].title, style="pluscredits_title_xsmall", xalign=0.5, yalign=0.4))
image pluscredits_TS_production_creative_director_n = AlphaMask("plusgrad1", Text(plus_credits['TS_production_creative_director'].name, style="pluscredits_name_xsmall", xalign=0.5, yalign=0.5))
image pluscredits_TS_production_art_consult_t = AlphaMask("plusgrad1", Text(plus_credits['TS_production_art_consult'].title, style="pluscredits_title_xsmall", xalign=0.5, yalign=0.4))
image pluscredits_TS_production_art_consult_n = AlphaMask("plusgrad1", Text(plus_credits['TS_production_art_consult'].name, style="pluscredits_name_xsmall", xalign=0.5, yalign=0.5))
image pluscredits_TS_production_project_management_t = AlphaMask("plusgrad1", Text(plus_credits['TS_production_project_management'].title, style="pluscredits_title_xsmall", xalign=0.5, yalign=0.4))
image pluscredits_TS_production_project_management_n = AlphaMask("plusgrad1", Text(plus_credits['TS_production_project_management'].name, style="pluscredits_name_xsmall", xalign=0.5, yalign=0.5))
image pluscredits_TS_production_community_management_t = AlphaMask("plusgrad1", Text(plus_credits['TS_production_community_management'].title, style="pluscredits_title_xsmall", xalign=0.5, yalign=0.4))
image pluscredits_TS_production_community_management_n = AlphaMask("plusgrad1", Text(plus_credits['TS_production_community_management'].name, style="pluscredits_name_xsmall", xalign=0.5, yalign=0.5))
image pluscredits_TS_production_image_gallery_l_t = AlphaMask("plusgrad1", Text(plus_credits['TS_production_image_gallery_l'].title, style="pluscredits_title_xsmall", xalign=0.5, yalign=0.4))
image pluscredits_TS_production_image_gallery_l_n = AlphaMask("plusgrad1", Text(plus_credits['TS_production_image_gallery_l'].name, style="pluscredits_name_xsmall", xalign=0.5, yalign=0.5))
image pluscredits_TS_production_image_gallery_r_t = AlphaMask("plusgrad1", Text(plus_credits['TS_production_image_gallery_r'].title, style="pluscredits_title_xsmall", xalign=0.5, yalign=0.4))
image pluscredits_TS_production_image_gallery_r_n = AlphaMask("plusgrad1", Text(plus_credits['TS_production_image_gallery_r'].name, style="pluscredits_name_xsmall", xalign=0.5, yalign=0.5))
image pluscredits_TS_production_promo_art_t = AlphaMask("plusgrad1", Text(plus_credits['TS_production_promo_art'].title, style="pluscredits_title_xsmall", xalign=0.5, yalign=0.4))
image pluscredits_TS_production_promo_art_n = AlphaMask("plusgrad1", Text(plus_credits['TS_production_promo_art'].name, style="pluscredits_name_xsmall", xalign=0.5, yalign=0.5))

image pluscredits_SF_title_t = AlphaMask("plusgrad1", Text(plus_credits['SF_title'].title, style="pluscredits_title_u", xalign=0.5, yalign=0.4))
image pluscredits_SF_title_n = AlphaMask("plusgrad1", Text(plus_credits['SF_title'].name, style="pluscredits_title_u", xalign=0.5, yalign=0.5))
image pluscredits_SF_executive_director_t = AlphaMask("plusgrad1", Text(plus_credits['SF_executive_director'].title, style="pluscredits_title", xalign=0.5, yalign=0.4))
image pluscredits_SF_executive_director_n = AlphaMask("plusgrad1", Text(plus_credits['SF_executive_director'].name, style="pluscredits_name", xalign=0.5, yalign=0.5))
image pluscredits_SF_publishing_director_t = AlphaMask("plusgrad1", Text(plus_credits['SF_publishing_director'].title, style="pluscredits_title", xalign=0.5, yalign=0.4))
image pluscredits_SF_publishing_director_n = AlphaMask("plusgrad1", Text(plus_credits['SF_publishing_director'].name, style="pluscredits_name", xalign=0.5, yalign=0.5))
image pluscredits_SF_lead_producer_t = AlphaMask("plusgrad1", Text(plus_credits['SF_lead_producer'].title, style="pluscredits_title", xalign=0.5, yalign=0.4))
image pluscredits_SF_lead_producer_n = AlphaMask("plusgrad1", Text(plus_credits['SF_lead_producer'].name, style="pluscredits_name", xalign=0.5, yalign=0.5))
image pluscredits_SF_production_manager_t = AlphaMask("plusgrad1", Text(plus_credits['SF_production_manager'].title, style="pluscredits_title", xalign=0.5, yalign=0.4))
image pluscredits_SF_production_manager_n = AlphaMask("plusgrad1", Text(plus_credits['SF_production_manager'].name, style="pluscredits_name", xalign=0.5, yalign=0.5))
image pluscredits_SF_lead_physical_pub_producer_t = AlphaMask("plusgrad1", Text(plus_credits['SF_lead_physical_pub_producer'].title, style="pluscredits_title", xalign=0.5, yalign=0.4))
image pluscredits_SF_lead_physical_pub_producer_n = AlphaMask("plusgrad1", Text(plus_credits['SF_lead_physical_pub_producer'].name, style="pluscredits_name", xalign=0.5, yalign=0.5))

image pluscredits_SF_lead_publishing_artist_t = AlphaMask("plusgrad1", Text(plus_credits['SF_lead_publishing_artist'].title, style="pluscredits_title_xsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_lead_publishing_artist_n = AlphaMask("plusgrad1", Text(plus_credits['SF_lead_publishing_artist'].name, style="pluscredits_name_xsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_graphic_designers_t = AlphaMask("plusgrad1", Text(plus_credits['SF_graphic_designers'].title, style="pluscredits_title_xsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_graphic_designers_n = AlphaMask("plusgrad1", Text(plus_credits['SF_graphic_designers'].name, style="pluscredits_name_xsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_product_designers_t = AlphaMask("plusgrad1", Text(plus_credits['SF_product_designers'].title, style="pluscredits_title_xsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_product_designers_n = AlphaMask("plusgrad1", Text(plus_credits['SF_product_designers'].name, style="pluscredits_name_xsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_lead_publishing_tech_t = AlphaMask("plusgrad1", Text(plus_credits['SF_lead_publishing_tech'].title, style="pluscredits_title_xsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_lead_publishing_tech_n = AlphaMask("plusgrad1", Text(plus_credits['SF_lead_publishing_tech'].name, style="pluscredits_name_xsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_porting_engineer_t = AlphaMask("plusgrad1", Text(plus_credits['SF_porting_engineer'].title, style="pluscredits_title_xsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_porting_engineer_n = AlphaMask("plusgrad1", Text(plus_credits['SF_porting_engineer'].name, style="pluscredits_name_xsmall", xalign=0.5, yalign=0.5))

image pluscredits_SF_marketing_director_t = AlphaMask("plusgrad1", Text(plus_credits['SF_marketing_director'].title, style="pluscredits_title_xsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_marketing_director_n = AlphaMask("plusgrad1", Text(plus_credits['SF_marketing_director'].name, style="pluscredits_name_xsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_marketing_manager_t = AlphaMask("plusgrad1", Text(plus_credits['SF_marketing_manager'].title, style="pluscredits_title_xsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_marketing_manager_n = AlphaMask("plusgrad1", Text(plus_credits['SF_marketing_manager'].name, style="pluscredits_name_xsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_publishing_producers_t = AlphaMask("plusgrad1", Text(plus_credits['SF_publishing_producers'].title, style="pluscredits_title_xsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_publishing_producers_n = AlphaMask("plusgrad1", Text(plus_credits['SF_publishing_producers'].name, style="pluscredits_name_xsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_media_director_t = AlphaMask("plusgrad1", Text(plus_credits['SF_media_director'].title, style="pluscredits_title_xsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_media_director_n = AlphaMask("plusgrad1", Text(plus_credits['SF_media_director'].name, style="pluscredits_name_xsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_marketing_associate_t = AlphaMask("plusgrad1", Text(plus_credits['SF_marketing_associate'].title, style="pluscredits_title_xsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_marketing_associate_n = AlphaMask("plusgrad1", Text(plus_credits['SF_marketing_associate'].name, style="pluscredits_name_xsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_PR_t = AlphaMask("plusgrad1", Text(plus_credits['SF_PR'].title, style="pluscredits_title_xsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_PR_n = AlphaMask("plusgrad1", Text(plus_credits['SF_PR'].name, style="pluscredits_name_xsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_website_development_t = AlphaMask("plusgrad1", Text(plus_credits['SF_website_development'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_website_development_n = AlphaMask("plusgrad1", Text(plus_credits['SF_website_development'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_community_moderator_n = AlphaMask("plusgrad1", Text(plus_credits['SF_community_moderator'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_community_moderator_t = AlphaMask("plusgrad1", Text(plus_credits['SF_community_moderator'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))

image pluscredits_SF_community_manager_t = AlphaMask("plusgrad1", Text(plus_credits['SF_community_manager'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_community_manager_n = AlphaMask("plusgrad1", Text(plus_credits['SF_community_manager'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_QA_lead_t = AlphaMask("plusgrad1", Text(plus_credits['SF_QA_lead'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_QA_lead_n = AlphaMask("plusgrad1", Text(plus_credits['SF_QA_lead'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_QA_t = AlphaMask("plusgrad1", Text(plus_credits['SF_QA'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_QA_n = AlphaMask("plusgrad1", Text(plus_credits['SF_QA'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_rating_associate_t = AlphaMask("plusgrad1", Text(plus_credits['SF_rating_associate'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_rating_associate_n = AlphaMask("plusgrad1", Text(plus_credits['SF_rating_associate'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_business_director_t = AlphaMask("plusgrad1", Text(plus_credits['SF_business_director'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_business_director_n = AlphaMask("plusgrad1", Text(plus_credits['SF_business_director'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_sales_finance_director_t = AlphaMask("plusgrad1", Text(plus_credits['SF_sales_finance_director'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_sales_finance_director_n = AlphaMask("plusgrad1", Text(plus_credits['SF_sales_finance_director'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_strategic_init_manager_t = AlphaMask("plusgrad1", Text(plus_credits['SF_strategic_init_manager'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_strategic_init_manager_n = AlphaMask("plusgrad1", Text(plus_credits['SF_strategic_init_manager'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_finance_analyst_t = AlphaMask("plusgrad1", Text(plus_credits['SF_finance_analyst'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_finance_analyst_n = AlphaMask("plusgrad1", Text(plus_credits['SF_finance_analyst'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_legal_t = AlphaMask("plusgrad1", Text(plus_credits['SF_legal'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_legal_n = AlphaMask("plusgrad1", Text(plus_credits['SF_legal'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_additional_support_t = AlphaMask("plusgrad1", Text(plus_credits['SF_additional_support_l'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_SF_additional_support_l_n = AlphaMask("plusgrad1", Text(plus_credits['SF_additional_support_l'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))
image pluscredits_SF_additional_support_r_n = AlphaMask("plusgrad1", Text(plus_credits['SF_additional_support_r'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))

image pluscredits_Localization_title_t = AlphaMask("plusgrad1", Text(plus_credits['Localization_title'].title, style="pluscredits_title_u", xalign=0.5, yalign=0.4))
image pluscredits_Localization_title_n = AlphaMask("plusgrad1", Text(plus_credits['Localization_title'].name, style="pluscredits_title_u", xalign=0.5, yalign=0.5))
image pluscredits_RL_title_t = AlphaMask("plusgrad1", Text(plus_credits['RL_title'].title, style="pluscredits_title", xalign=0.5, yalign=0.4))
image pluscredits_RL_title_n = AlphaMask("plusgrad1", Text(plus_credits['RL_title'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_RL_project_management_t = AlphaMask("plusgrad1", Text(plus_credits['RL_project_management'].title, style="pluscredits_title_xxxsmall", xalign=0.5, yalign=0.4))
image pluscredits_RL_project_management_n = AlphaMask("plusgrad1", Text(plus_credits['RL_project_management'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_RL_french_t = AlphaMask("plusgrad1", Text(plus_credits['RL_french'].title, style="pluscredits_title_xxxsmall", xalign=0.5, yalign=0.4))
image pluscredits_RL_french_n = AlphaMask("plusgrad1", Text(plus_credits['RL_french'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_RL_german_t = AlphaMask("plusgrad1", Text(plus_credits['RL_german'].title, style="pluscredits_title_xxxsmall", xalign=0.5, yalign=0.4))
image pluscredits_RL_german_n = AlphaMask("plusgrad1", Text(plus_credits['RL_german'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_RL_italian_t = AlphaMask("plusgrad1", Text(plus_credits['RL_italian'].title, style="pluscredits_title_xxxsmall", xalign=0.5, yalign=0.4))
image pluscredits_RL_italian_n = AlphaMask("plusgrad1", Text(plus_credits['RL_italian'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_RL_japanese_t = AlphaMask("plusgrad1", Text(plus_credits['RL_japanese'].title, style="pluscredits_title_xxxsmall", xalign=0.5, yalign=0.4))
image pluscredits_RL_japanese_n = AlphaMask("plusgrad1", Text(plus_credits['RL_japanese'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_RL_korean_t = AlphaMask("plusgrad1", Text(plus_credits['RL_korean'].title, style="pluscredits_title_xxxsmall", xalign=0.5, yalign=0.4))
image pluscredits_RL_korean_n = AlphaMask("plusgrad1", Text(plus_credits['RL_korean'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_RL_portuguese_t = AlphaMask("plusgrad1", Text(plus_credits['RL_portuguese'].title, style="pluscredits_title_xxxsmall", xalign=0.5, yalign=0.4))
image pluscredits_RL_portuguese_n = AlphaMask("plusgrad1", Text(plus_credits['RL_portuguese'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_RL_russian_t = AlphaMask("plusgrad1", Text(plus_credits['RL_russian'].title, style="pluscredits_title_xxxsmall", xalign=0.5, yalign=0.4))
image pluscredits_RL_russian_n = AlphaMask("plusgrad1", Text(plus_credits['RL_russian'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_RL_spanish_t = AlphaMask("plusgrad1", Text(plus_credits['RL_spanish'].title, style="pluscredits_title_xxxsmall", xalign=0.5, yalign=0.4))
image pluscredits_RL_spanish_n = AlphaMask("plusgrad1", Text(plus_credits['RL_spanish'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_RL_chinese_t = AlphaMask("plusgrad1", Text(plus_credits['RL_chinese'].title, style="pluscredits_title_xxxsmall", xalign=0.5, yalign=0.4))
image pluscredits_RL_chinese_n = AlphaMask("plusgrad1", Text(plus_credits['RL_chinese'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Fan_translation_support_title_t = AlphaMask("plusgrad1", Text(plus_credits['Fan_translation_support_title'].title, style="pluscredits_title", xalign=0.5, yalign=0.4))
image pluscredits_Fan_translation_support_title_n = AlphaMask("plusgrad1", Text(plus_credits['Fan_translation_support_title'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Fan_translation_simp_chinese_t = AlphaMask("plusgrad1", Text(plus_credits['Fan_translation_simp_chinese'].title, style="pluscredits_title_xxxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Fan_translation_simp_chinese_n = AlphaMask("plusgrad1", Text(plus_credits['Fan_translation_simp_chinese'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Fan_translation_trad_chinese_t = AlphaMask("plusgrad1", Text(plus_credits['Fan_translation_trad_chinese'].title, style="pluscredits_title_xxxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Fan_translation_trad_chinese_n = AlphaMask("plusgrad1", Text(plus_credits['Fan_translation_trad_chinese'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Fan_translation_japanese_t = AlphaMask("plusgrad1", Text(plus_credits['Fan_translation_japanese'].title, style="pluscredits_title_xxxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Fan_translation_japanese_n = AlphaMask("plusgrad1", Text(plus_credits['Fan_translation_japanese'].name, style="pluscredits_name_xxxsmall", font="NotoSansCJKjp-Regular.otf", xalign=0.5, yalign=0.5))

image pluscredits_Altagram_title_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_title'].title, style="pluscredits_title_u", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_title_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_title'].name, style="pluscredits_title_u", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_production_title_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_production_title'].title, style="pluscredits_title_u_small", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_production_title_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_production_title'].name, style="pluscredits_title_u_small", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_production_PM_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_production_PM'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_production_PM_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_production_PM'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_production_SLE_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_production_SLE'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_production_SLE_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_production_SLE'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_production_LE_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_production_LE'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_production_LE_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_production_LE'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_french_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_french'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_french_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_french'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_german_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_german'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_german_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_german'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_portugese_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_portugese'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_portugese_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_portugese'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_spanishLA_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_spanishLA'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_spanishLA_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_spanishLA'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_spanishSP_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_spanishSP'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_spanishSP_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_spanishSP'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_italian_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_italian'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_italian_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_italian'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_japanese_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_japanese'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_japanese_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_japanese'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_korean_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_korean'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_korean_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_korean'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_chineseSM_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_chineseSM'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_chineseSM_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_chineseSM'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_chineseTR_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_chineseTR'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_chineseTR_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_chineseTR'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_project_manager_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_project_manager'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_project_manager_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_project_manager'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_linguistic_lead_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_linguistic_lead'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_linguistic_lead_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_linguistic_lead'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_partnership_manager_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_partnership_manager'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_partnership_manager_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_partnership_manager'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_cco_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_cco'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_cco_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_cco'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_coo_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_coo'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_coo_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_coo'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Altagram_ceo_t = AlphaMask("plusgrad1", Text(plus_credits['Altagram_ceo'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Altagram_ceo_n = AlphaMask("plusgrad1", Text(plus_credits['Altagram_ceo'].name, style="pluscredits_name_xxxsmall", xalign=0.5, yalign=0.5))

image pluscredits_Creative_artists_agency_t = AlphaMask("plusgrad1", Text(plus_credits['Creative_artists_agency'].title, style="pluscredits_title_u_small", xalign=0.5, yalign=0.4))
image pluscredits_Creative_artists_agency_n = AlphaMask("plusgrad1", Text(plus_credits['Creative_artists_agency'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Special_thanks_l_t = AlphaMask("plusgrad1", Text(plus_credits['Special_thanks_l'].title, style="pluscredits_title_u", xalign=0.5, yalign=0.4))
image pluscredits_Special_thanks_l_n = AlphaMask("plusgrad1", Text(plus_credits['Special_thanks_l'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Special_thanks_r_t = AlphaMask("plusgrad1", Text(plus_credits['Special_thanks_r'].title, style="pluscredits_title_xxsmall", xalign=0.5, yalign=0.4))
image pluscredits_Special_thanks_r_n = AlphaMask("plusgrad1", Text(plus_credits['Special_thanks_r'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))
image pluscredits_Special_thanks_l_n_mobile = AlphaMask("plusgrad1", Text(plus_credits['Special_thanks_l'].name+"\n"+plus_credits['Special_thanks_mobile'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))

image pluscredits_End_thanks_t = AlphaMask("plusgrad1", Text(plus_credits['End_thanks'].title, style="pluscredits_title", xalign=0.5, yalign=0.4))
image pluscredits_End_thanks_n = AlphaMask("plusgrad1", Text(plus_credits['End_thanks'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))
image pluscredits_End_love_t = AlphaMask("plusgrad1", Text(plus_credits['End_love'].title, style="pluscredits_title", xalign=0.5, yalign=0.4, size=28))
image pluscredits_End_love_n = AlphaMask("plusgrad1", Text(plus_credits['End_love'].name, style="pluscredits_name_xxsmall", xalign=0.5, yalign=0.5))

image pluscredits_thanks = ParameterizedText(style="pluscredits_thanks", xalign=0.5, yalign=0.7)

style pluscredits_title:
    font gui.virtual_desktop_bold_text_font
    color "#000"
    size 22
    text_align 0.5
    outlines []
style pluscredits_title_large is pluscredits_title:
    size 34
style pluscredits_title_small is pluscredits_title:
    size 20
style pluscredits_title_xsmall is pluscredits_title:
    size 18
style pluscredits_title_xxsmall is pluscredits_title:
    size 16
style pluscredits_title_xxxsmall is pluscredits_title:
    size 14

style pluscredits_title_u:
    font gui.virtual_desktop_bold_text_font
    color "#000"
    size 44
    text_align 0.5
    outlines []
    underline True
style pluscredits_title_u_small is pluscredits_title_u:
    size 34

style pluscredits_ts_style:
    font gui.virtual_desktop_bold_text_font
    color "#000"
    size 14
    text_align 0.5
    outlines []

style pluscredits_name:
    font gui.virtual_desktop_bold_text_font
    color "#000"
    size 34
    text_align 0.5
    outlines []
style pluscredits_name_small is pluscredits_name:
    size 30
style pluscredits_name_xsmall is pluscredits_name:
    size 26
style pluscredits_name_xxsmall is pluscredits_name:
    size 20
style pluscredits_name_xxxsmall is pluscredits_name:
    size 14

style pluscredits_thanks:
    font gui.virtual_desktop_bold_text_font
    color "#402"
    size 14
    text_align 0.5
    outlines []

transform pluscredits_left(direction=1):
    subpixel True
    xpos 400 * direction
    xoffset 60 * direction
    linear 9.5 xoffset -60 * direction
transform pluscredits_right:
    pluscredits_left(-1)

transform pluscredits_name_left(direction=1):
    subpixel True
    xalign 0.5
    xoffset 160 * direction
    alpha 0
    parallel:
        easein_cubic 5 xoffset 240 * direction
    parallel:
        easein_cubic 4.0 alpha 1
    2
    parallel:
        easeout_cubic 2 alpha 0
    parallel:
        easeout_cubic 2.25 xoffset 360 * direction
transform pluscredits_name_right:
    pluscredits_name_left(-1)

transform pluscredits_name_left_switch(direction=1):
    subpixel True
    xalign 0.5
    xoffset 320 * direction
    alpha 0
    parallel:
        easein_cubic 5 xoffset 240 * direction
    parallel:
        easein_cubic 4.0 alpha 1
    2
    parallel:
        easeout_cubic 2 alpha 0
    parallel:
        easeout_cubic 2.25 xoffset 160 * direction
transform pluscredits_name_right_switch:
    pluscredits_name_left_switch(-1)

transform pluscredits_final_thanks:
    subpixel True
    xalign 0.5
    xoffset -320
    alpha 0
    parallel:
        easein_cubic 5 xoffset -240
    parallel:
        easein_cubic 3.0 alpha 1
    2.75
    ease_cubic 2.5 xoffset 0
    0.5
    easeout_cubic 0.5 alpha 0

transform reveal_cg_left(direction=1):
    subpixel True
    xoffset 0
    easein_cubic 5 xoffset 480 * direction
    2
    easeout_cubic 2.5 xoffset 0 * direction
transform reveal_cg_right:
    reveal_cg_left(-1)

transform pluscredits_ts_transform:
    xalign 0.5
    alpha 0
    linear 1.0 alpha 1
    2.0
    linear 1.0 alpha 0

label pluscredits_start:
    $ unlock("bgm_sofal")
    play music p10 noloop
    $ starttime = datetime.datetime.now()
    show black zorder 1:
        alpha 0
        linear 3 alpha 1
    $ pause(0.5)
    scene black with Dissolve(3)
    $ pause(3)
    scene bg corridor with Dissolve(3)
    $ pause(3)
    scene bg residential_day with Dissolve(3)
    $ pause(3)
    scene white
    show pluscredits_game_title_t zorder 3:
        subpixel True
        xpos 120
        xoffset 60
        parallel:
            linear 9.5 xoffset -60
    with Dissolve(3)
    $ pause(0.4)
    hide pluscredits_game_title_t with Dissolve(1.1)
    jump pluscredits

label pluscredits:
    $ starttime = datetime.datetime.now()
    $ cgcount = 0
    show white zorder 2
    show pluscredits_cg1 as pluscredits_cg at pluscredits_right
    show pluscredits_written_and_directed_t zorder 3 at pluscredits_name_left
    show pluscredits_written_and_directed_n zorder 3 at pluscredits_name_left
    show white at reveal_cg_left

    $ cgcount += 1
    $ pause(9.6)
    hide pluscredits_cg
    hide pluscredits_name
    hide pluscredits_title
    show white at reveal_cg_right
    show pluscredits_cg2 as pluscredits_cg at pluscredits_left
    show pluscredits_TS_development_title_t zorder 3 at pluscredits_name_right_switch:
        yoffset -200
    $ pause(0.2)
    show pluscredits_TS_development_art_1_t zorder 3 at pluscredits_name_right:
        yoffset -100
    show pluscredits_TS_development_art_1_n zorder 3 at pluscredits_name_right:
        yoffset -110
    $ pause(0.2)
    show pluscredits_TS_development_art_2_t zorder 3 at pluscredits_name_right:
        yoffset 40
    show pluscredits_TS_development_art_2_n zorder 3 at pluscredits_name_right:
        yoffset 30
    $ pause(0.2)
    show pluscredits_TS_development_art_3_t zorder 3 at pluscredits_name_right:
        yoffset 200
    show pluscredits_TS_development_art_3_n zorder 3 at pluscredits_name_right:
        yoffset 170

    $ cgcount += 1
    $ pause(9.6)
    hide pluscredits_cg
    hide pluscredits_name
    hide pluscredits_title
    show white at reveal_cg_left
    show pluscredits_cg3 as pluscredits_cg at pluscredits_right
    show pluscredits_TS_development_programming_t zorder 3 at pluscredits_name_left:
        yoffset -200
    show pluscredits_TS_development_programming_n zorder 3 at pluscredits_name_left:
        yoffset -230
    $ pause(0.2)
    show pluscredits_TS_development_UI_design_t zorder 3 at pluscredits_name_left:
        yoffset -90
    show pluscredits_TS_development_UI_design_n zorder 3 at pluscredits_name_left:
        yoffset -100
    $ pause(0.2)
    show pluscredits_TS_development_music_1_t zorder 3 at pluscredits_name_left:
        yoffset 50
    show pluscredits_TS_development_music_1_n zorder 3 at pluscredits_name_left:
        yoffset 20
    $ pause(0.2)
    show pluscredits_TS_development_music_2_t zorder 3 at pluscredits_name_left:
        yoffset 160
    show pluscredits_TS_development_music_2_n zorder 3 at pluscredits_name_left:
        yoffset 130
    $ pause(0.2)
    show pluscredits_TS_development_music_3_t zorder 3 at pluscredits_name_left:
        yoffset 270
    show pluscredits_TS_development_music_3_n zorder 3 at pluscredits_name_left:
        yoffset 260

    $ cgcount += 1
    $ pause(9.6)

    hide pluscredits_TS_development_title_t
    hide pluscredits_TS_development_art_1_t
    hide pluscredits_TS_development_art_1_n
    hide pluscredits_TS_development_art_2_t
    hide pluscredits_TS_development_art_2_n
    hide pluscredits_TS_development_art_3_t
    hide pluscredits_TS_development_art_3_n

    hide pluscredits_cg
    hide pluscredits_name
    hide pluscredits_title
    show white at reveal_cg_right
    show pluscredits_cg4 as pluscredits_cg at pluscredits_left
    show pluscredits_TS_production_title_t zorder 3 at pluscredits_name_right_switch:
        yoffset -240
    $ pause(0.2)
    show pluscredits_TS_production_creative_director_t zorder 3 at pluscredits_name_right:
        yoffset -180
    show pluscredits_TS_production_creative_director_n zorder 3 at pluscredits_name_right:
        yoffset -220
    $ pause(0.2)
    show pluscredits_TS_production_art_consult_t zorder 3 at pluscredits_name_right:
        yoffset -100
    show pluscredits_TS_production_art_consult_n zorder 3 at pluscredits_name_right:
        yoffset -140
    $ pause(0.2)
    show pluscredits_TS_production_project_management_t zorder 3 at pluscredits_name_right:
        yoffset -10
    show pluscredits_TS_production_project_management_n zorder 3 at pluscredits_name_right:
        yoffset -50
    $ pause(0.2)
    show pluscredits_TS_production_community_management_t zorder 3 at pluscredits_name_right:
        yoffset 80
    show pluscredits_TS_production_community_management_n zorder 3 at pluscredits_name_right:
        yoffset 40
    $ pause(0.2)
    show pluscredits_TS_production_image_gallery_l_t zorder 3 at pluscredits_name_right:
        yoffset 170
    show pluscredits_TS_production_image_gallery_l_n zorder 3 at pluscredits_name_right:
        yoffset 150
        xoffset -100
    show pluscredits_TS_production_image_gallery_r_n zorder 3 at pluscredits_name_right:
        yoffset 150
        xoffset 100
    $ pause(0.2)
    show pluscredits_TS_production_promo_art_t zorder 3 at pluscredits_name_right:
        yoffset 280
    show pluscredits_TS_production_promo_art_n zorder 3 at pluscredits_name_right:
        yoffset 270


    $ cgcount += 1
    $ pause(9.6)

    hide pluscredits_TS_development_programming_t
    hide pluscredits_TS_development_programming_n
    hide pluscredits_TS_development_UI_design_t
    hide pluscredits_TS_development_UI_design_n
    hide pluscredits_TS_development_music_1_t
    hide pluscredits_TS_development_music_1_n
    hide pluscredits_TS_development_music_2_t
    hide pluscredits_TS_development_music_2_n
    hide pluscredits_TS_development_music_3_t
    hide pluscredits_TS_development_music_3_n

    hide pluscredits_cg
    hide pluscredits_name
    hide pluscredits_title
    show white at reveal_cg_left
    show pluscredits_cg5 as pluscredits_cg at pluscredits_right
    show pluscredits_SF_title_t zorder 3 at pluscredits_name_left_switch:
        yoffset -200
    $ pause(0.2)
    show pluscredits_SF_executive_director_t zorder 3 at pluscredits_name_left:
        yoffset -100
    show pluscredits_SF_executive_director_n zorder 3 at pluscredits_name_left:
        yoffset -130
    $ pause(0.2)
    show pluscredits_SF_publishing_director_t zorder 3 at pluscredits_name_left:
        yoffset 10
    show pluscredits_SF_publishing_director_n zorder 3 at pluscredits_name_left:
        yoffset -20
    $ pause(0.2)
    show pluscredits_SF_lead_producer_t zorder 3 at pluscredits_name_left:
        yoffset 110
    show pluscredits_SF_lead_producer_n zorder 3 at pluscredits_name_left:
        yoffset 80
    $ pause(0.2)
    show pluscredits_SF_production_manager_t zorder 3 at pluscredits_name_left:
        yoffset 210
    show pluscredits_SF_production_manager_n zorder 3 at pluscredits_name_left:
        yoffset 180
    $ pause(0.2)
    show pluscredits_SF_lead_physical_pub_producer_t zorder 3 at pluscredits_name_left:
        yoffset 320
    show pluscredits_SF_lead_physical_pub_producer_n zorder 3 at pluscredits_name_left:
        yoffset 290

    $ cgcount += 1
    $ pause(9.6)

    hide pluscredits_TS_production_title_t
    hide pluscredits_TS_production_creative_director_t
    hide pluscredits_TS_production_creative_director_n
    hide pluscredits_TS_production_art_consult_t
    hide pluscredits_TS_production_art_consult_n
    hide pluscredits_TS_production_project_management_t
    hide pluscredits_TS_production_project_management_n
    hide pluscredits_TS_production_community_management_t
    hide pluscredits_TS_production_community_management_n
    hide pluscredits_TS_production_image_gallery_l_t
    hide pluscredits_TS_production_image_gallery_l_n
    hide pluscredits_TS_production_image_gallery_r_n
    hide pluscredits_TS_production_promo_art_t
    hide pluscredits_TS_production_promo_art_n

    hide pluscredits_cg
    hide pluscredits_name
    hide pluscredits_title
    show white at reveal_cg_right
    show pluscredits_cg6 as pluscredits_cg at pluscredits_left
    show pluscredits_SF_lead_publishing_artist_t zorder 3 at pluscredits_name_right:
        yoffset -240
    show pluscredits_SF_lead_publishing_artist_n zorder 3 at pluscredits_name_right:
        yoffset -280
    $ pause(0.2)
    show pluscredits_SF_graphic_designers_t zorder 3 at pluscredits_name_right:
        yoffset -170
    show pluscredits_SF_graphic_designers_n zorder 3 at pluscredits_name_right:
        yoffset -150
    $ pause(0.2)
    show pluscredits_SF_product_designers_t zorder 3 at pluscredits_name_right:
        yoffset 30
    show pluscredits_SF_product_designers_n zorder 3 at pluscredits_name_right:
        yoffset 50
    $ pause(0.2)
    show pluscredits_SF_lead_publishing_tech_t zorder 3 at pluscredits_name_right:
        yoffset 230
    show pluscredits_SF_lead_publishing_tech_n zorder 3 at pluscredits_name_right:
        yoffset 190
    $ pause(0.2)
    show pluscredits_SF_porting_engineer_t zorder 3 at pluscredits_name_right:
        yoffset 300
    show pluscredits_SF_porting_engineer_n zorder 3 at pluscredits_name_right:
        yoffset 295

    $ cgcount += 1
    $ pause(9.6)

    hide pluscredits_SF_title_t
    hide pluscredits_SF_executive_director_t
    hide pluscredits_SF_executive_director_n
    hide pluscredits_SF_publishing_director_t
    hide pluscredits_SF_publishing_director_n
    hide pluscredits_SF_lead_producer_t
    hide pluscredits_SF_lead_producer_n
    hide pluscredits_SF_production_manager_t
    hide pluscredits_SF_production_manager_n
    hide pluscredits_SF_lead_physical_pub_producer_t
    hide pluscredits_SF_lead_physical_pub_producer_n

    hide pluscredits_cg
    hide pluscredits_name
    hide pluscredits_title
    show white at reveal_cg_left
    show pluscredits_cg7 as pluscredits_cg at pluscredits_right
    show pluscredits_SF_marketing_director_t zorder 3 at pluscredits_name_left:
        yoffset -240
    show pluscredits_SF_marketing_director_n zorder 3 at pluscredits_name_left:
        yoffset -280
    $ pause(0.2)
    show pluscredits_SF_marketing_manager_t zorder 3 at pluscredits_name_left:
        yoffset -170
    show pluscredits_SF_marketing_manager_n zorder 3 at pluscredits_name_left:
        yoffset -210
    $ pause(0.2)
    show pluscredits_SF_publishing_producers_t zorder 3 at pluscredits_name_left:
        yoffset -100
    show pluscredits_SF_publishing_producers_n zorder 3 at pluscredits_name_left:
        yoffset -120
    $ pause(0.2)
    show pluscredits_SF_media_director_t zorder 3 at pluscredits_name_left:
        yoffset 5
    show pluscredits_SF_media_director_n zorder 3 at pluscredits_name_left:
        yoffset -35
    $ pause(0.2)
    show pluscredits_SF_marketing_associate_t zorder 3 at pluscredits_name_left:
        yoffset 80
    show pluscredits_SF_marketing_associate_n zorder 3 at pluscredits_name_left:
        yoffset 50
    $ pause(0.2)
    show pluscredits_SF_website_development_t zorder 3 at pluscredits_name_left:
        yoffset 175
    show pluscredits_SF_website_development_n zorder 3 at pluscredits_name_left:
        yoffset 145
    $ pause(0.2)
    show pluscredits_SF_community_moderator_n zorder 3 at pluscredits_name_left:
        yoffset 190
    show pluscredits_SF_community_moderator_t zorder 3 at pluscredits_name_left:
        yoffset 265

    $ cgcount += 1
    $ pause(9.6)

    hide pluscredits_SF_lead_publishing_artist_t
    hide pluscredits_SF_lead_publishing_artist_n
    hide pluscredits_SF_graphic_designers_t
    hide pluscredits_SF_graphic_designers_n
    hide pluscredits_SF_product_designers_t
    hide pluscredits_SF_product_designers_n
    hide pluscredits_SF_lead_publishing_tech_t
    hide pluscredits_SF_lead_publishing_tech_n
    hide pluscredits_SF_porting_engineer_t
    hide pluscredits_SF_porting_engineer_n

    hide pluscredits_cg
    hide pluscredits_name
    hide pluscredits_title
    show white at reveal_cg_right
    show pluscredits_cg8 as pluscredits_cg at pluscredits_left
    show pluscredits_SF_community_manager_t zorder 3 at pluscredits_name_right:
        yoffset -240
    show pluscredits_SF_community_manager_n zorder 3 at pluscredits_name_right:
        yoffset -270
    $ pause(0.2)
    show pluscredits_SF_QA_lead_t zorder 3 at pluscredits_name_right:
        yoffset -155
    show pluscredits_SF_QA_lead_n zorder 3 at pluscredits_name_right:
        yoffset -200
    $ pause(0.2)
    show pluscredits_SF_QA_t zorder 3 at pluscredits_name_right:
        yoffset -95
    show pluscredits_SF_QA_n zorder 3 at pluscredits_name_right:
        yoffset -115
    $ pause(0.2)
    show pluscredits_SF_rating_associate_t zorder 3 at pluscredits_name_right:
        yoffset 15
    show pluscredits_SF_rating_associate_n zorder 3 at pluscredits_name_right:
        yoffset -30
    $ pause(0.2)
    show pluscredits_SF_business_director_t zorder 3 at pluscredits_name_right:
        yoffset 75
        xoffset -120
    show pluscredits_SF_business_director_n zorder 3 at pluscredits_name_right:
        yoffset 25
        xoffset -120
    $ pause(0.2)
    show pluscredits_SF_sales_finance_director_t zorder 3 at pluscredits_name_right:
        yoffset 75
        xoffset 120
    show pluscredits_SF_sales_finance_director_n zorder 3 at pluscredits_name_right:
        yoffset 40
        xoffset 120
    $ pause(0.2)
    show pluscredits_SF_strategic_init_manager_t zorder 3 at pluscredits_name_right:
        yoffset 150
        xoffset -120
    show pluscredits_SF_strategic_init_manager_n zorder 3 at pluscredits_name_right:
        yoffset 100
        xoffset -120
    $ pause(0.2)
    show pluscredits_SF_finance_analyst_t zorder 3 at pluscredits_name_right:
        yoffset 150
        xoffset 120
    show pluscredits_SF_finance_analyst_n zorder 3 at pluscredits_name_right:
        yoffset 100
        xoffset 120
    $ pause(0.2)
    show pluscredits_SF_legal_t zorder 3 at pluscredits_name_right:
        yoffset 200
    show pluscredits_SF_legal_n zorder 3 at pluscredits_name_right:
        yoffset 165
    $ pause(0.2)
    show pluscredits_SF_additional_support_t zorder 3 at pluscredits_name_right:
        yoffset 280
    show pluscredits_SF_additional_support_l_n zorder 3 at pluscredits_name_right:
        yoffset 270
        xoffset -120
    show pluscredits_SF_additional_support_r_n zorder 3 at pluscredits_name_right:
        yoffset 270
        xoffset 120

    $ cgcount += 1
    $ pause(9.6)

    hide pluscredits_SF_marketing_director_t
    hide pluscredits_SF_marketing_director_n
    hide pluscredits_SF_marketing_manager_t
    hide pluscredits_SF_marketing_manager_n
    hide pluscredits_SF_publishing_producers_t
    hide pluscredits_SF_publishing_producers_n
    hide pluscredits_SF_media_director_t
    hide pluscredits_SF_media_director_n
    hide pluscredits_SF_marketing_associate_t
    hide pluscredits_SF_marketing_associate_n
    hide pluscredits_SF_PR_t
    hide pluscredits_SF_PR_n
    hide pluscredits_SF_website_development_t
    hide pluscredits_SF_website_development_n
    hide pluscredits_SF_community_moderator_n
    hide pluscredits_SF_community_moderator_t

    hide pluscredits_cg
    hide pluscredits_name
    hide pluscredits_title
    show white at reveal_cg_left
    show pluscredits_cg9 as pluscredits_cg at pluscredits_right
    show pluscredits_Localization_title_t zorder 3 at pluscredits_name_left_switch:
        yoffset -240
    $ pause(0.1)
    show pluscredits_RL_title_t zorder 3 at pluscredits_name_left:
        yoffset -180
    $ pause(0.1)
    show pluscredits_RL_project_management_t zorder 3 at pluscredits_name_left:
        yoffset -140
        xanchor .7
    show pluscredits_RL_project_management_n zorder 3 at pluscredits_name_left:
        yoffset -180
        xanchor .7
    $ pause(0.1)
    show pluscredits_RL_korean_t zorder 3 at pluscredits_name_left:
        yoffset -140
        xanchor .3
    show pluscredits_RL_korean_n zorder 3 at pluscredits_name_left:
        yoffset -192
        xanchor .3
    $ pause(0.1)
    show pluscredits_RL_french_t zorder 3 at pluscredits_name_left:
        yoffset -50
        xanchor .7
    show pluscredits_RL_french_n zorder 3 at pluscredits_name_left:
        yoffset -90
        xanchor .7
    $ pause(0.1)
    show pluscredits_RL_portuguese_t zorder 3 at pluscredits_name_left:
        yoffset -50
        xanchor .3
    show pluscredits_RL_portuguese_n zorder 3 at pluscredits_name_left:
        yoffset -90
        xanchor .3
    $ pause(0.1)
    show pluscredits_RL_german_t zorder 3 at pluscredits_name_left:
        yoffset 40
        xanchor .7
    show pluscredits_RL_german_n zorder 3 at pluscredits_name_left:
        yoffset 0
        xanchor .7
    $ pause(0.1)
    show pluscredits_RL_russian_t zorder 3 at pluscredits_name_left:
        yoffset 40
        xanchor .3
    show pluscredits_RL_russian_n zorder 3 at pluscredits_name_left:
        yoffset -8
        xanchor .3
    $ pause(0.1)
    show pluscredits_RL_italian_t zorder 3 at pluscredits_name_left:
        yoffset 130
        xanchor .7
    show pluscredits_RL_italian_n zorder 3 at pluscredits_name_left:
        yoffset 90
        xanchor .7
    $ pause(0.1)
    show pluscredits_RL_spanish_t zorder 3 at pluscredits_name_left:
        yoffset 130
        xanchor .3
    show pluscredits_RL_spanish_n zorder 3 at pluscredits_name_left:
        yoffset 90
        xanchor .3
    $ pause(0.1)
    show pluscredits_RL_japanese_t zorder 3 at pluscredits_name_left:
        yoffset 220
        xanchor .7
    show pluscredits_RL_japanese_n zorder 3 at pluscredits_name_left:
        yoffset 170
        xanchor .7
    $ pause(0.1)
    show pluscredits_RL_chinese_t zorder 3 at pluscredits_name_left:
        yoffset 220
        xanchor .3
    show pluscredits_RL_chinese_n zorder 3 at pluscredits_name_left:
        yoffset 180
        xanchor .3

    $ cgcount += 1
    $ pause(9.6)

    hide pluscredits_SF_community_manager_t
    hide pluscredits_SF_community_manager_n
    hide pluscredits_SF_QA_lead_t
    hide pluscredits_SF_QA_lead_n
    hide pluscredits_SF_QA_t
    hide pluscredits_SF_QA_n
    hide pluscredits_SF_rating_associate_t
    hide pluscredits_SF_rating_associate_n
    hide pluscredits_SF_business_director_t
    hide pluscredits_SF_business_director_n
    hide pluscredits_SF_sales_finance_director_t
    hide pluscredits_SF_sales_finance_director_n
    hide pluscredits_SF_rating_associate_t
    hide pluscredits_SF_rating_associate_n
    hide pluscredits_SF_strategic_init_manager_t
    hide pluscredits_SF_strategic_init_manager_n
    hide pluscredits_SF_legal_t
    hide pluscredits_SF_legal_n
    hide pluscredits_SF_additional_support_t
    hide pluscredits_SF_additional_support_n

    hide pluscredits_cg
    hide pluscredits_name
    hide pluscredits_title
    show white at reveal_cg_right
    show pluscredits_cg10 as pluscredits_cg at pluscredits_left
    show pluscredits_Fan_translation_support_title_t zorder 3 at pluscredits_name_right:
        yoffset -220
    show pluscredits_Fan_translation_simp_chinese_t zorder 3 at pluscredits_name_right:
        yoffset -180
    show pluscredits_Fan_translation_simp_chinese_n zorder 3 at pluscredits_name_right:
        yoffset -230
    $ pause(0.1)
    show pluscredits_Fan_translation_trad_chinese_t zorder 3 at pluscredits_name_right:
        yoffset -130
    show pluscredits_Fan_translation_trad_chinese_n zorder 3 at pluscredits_name_right:
        yoffset -180
    $ pause(0.1)
    show pluscredits_Fan_translation_japanese_t zorder 3 at pluscredits_name_right:
        yoffset -80
    show pluscredits_Fan_translation_japanese_n zorder 3 at pluscredits_name_right:
        yoffset -130
    show pluscredits_Creative_artists_agency_t zorder 3 at pluscredits_name_right:
        yoffset -20
    show pluscredits_Creative_artists_agency_n zorder 3 at pluscredits_name_right:
        yoffset -30
    $ pause(0.2)
    show pluscredits_Special_thanks_l_t zorder 3 at pluscredits_name_right:
        yoffset 100
    if renpy.mobile:
        show pluscredits_Special_thanks_l_n_mobile zorder 3 at pluscredits_name_right:
            yoffset 180
            xanchor .65
    else:
        show pluscredits_Special_thanks_l_n zorder 3 at pluscredits_name_right:
            yoffset 180
            xanchor .65
    show pluscredits_Special_thanks_r_n zorder 3 at pluscredits_name_right:
        yoffset 180
        xanchor .35

    $ cgcount += 1
    $ pause(9.6)

    hide pluscredits_Localization_title_t
    hide pluscredits_RL_title_t
    hide pluscredits_RL_project_management_t
    hide pluscredits_RL_project_management_n
    hide pluscredits_RL_korean_t
    hide pluscredits_RL_korean_n
    hide pluscredits_RL_french_t
    hide pluscredits_RL_french_n
    hide pluscredits_RL_portuguese_t
    hide pluscredits_RL_portuguese_n
    hide pluscredits_RL_german_t
    hide pluscredits_RL_german_n
    hide pluscredits_RL_russian_t
    hide pluscredits_RL_russian_n
    hide pluscredits_RL_italian_t
    hide pluscredits_RL_italian_n
    hide pluscredits_RL_spanish_t
    hide pluscredits_RL_spanish_n
    hide pluscredits_RL_japanese_t
    hide pluscredits_RL_japanese_n
    hide pluscredits_RL_chinese_t
    hide pluscredits_RL_chinese_n

    hide pluscredits_cg
    hide pluscredits_name
    hide pluscredits_title
    show white at reveal_cg_left
    show pluscredits_cg11 as pluscredits_cg at pluscredits_right
    show pluscredits_Altagram_title_t zorder 3 at pluscredits_name_left_switch:
        yoffset -240
    $ pause(0.1)
    show pluscredits_Altagram_production_title_t zorder 3 at pluscredits_name_left:
        yoffset -180
    $ pause(0.1)
    show pluscredits_Altagram_production_PM_t zorder 3 at pluscredits_name_left:
        yoffset -140
        xanchor .25
    show pluscredits_Altagram_production_PM_n zorder 3 at pluscredits_name_left:
        yoffset -180
        xanchor .25
    $ pause(0.1)
    show pluscredits_Altagram_production_SLE_t zorder 3 at pluscredits_name_left:
        yoffset -140
        xanchor .5
    show pluscredits_Altagram_production_SLE_n zorder 3 at pluscredits_name_left:
        yoffset -180
        xanchor .5
    $ pause(0.1)
    show pluscredits_Altagram_production_LE_t zorder 3 at pluscredits_name_left:
        yoffset -140
        xanchor .75
    show pluscredits_Altagram_production_LE_n zorder 3 at pluscredits_name_left:
        yoffset -180
        xanchor .75
    $ pause(0.1)
    show pluscredits_Altagram_french_t zorder 3 at pluscredits_name_left:
        yoffset -50
        xanchor .3
    show pluscredits_Altagram_french_n zorder 3 at pluscredits_name_left:
        yoffset -90
        xanchor .3
    $ pause(0.1)
    show pluscredits_Altagram_german_t zorder 3 at pluscredits_name_left:
        yoffset -50
        xanchor .5
    show pluscredits_Altagram_german_n zorder 3 at pluscredits_name_left:
        yoffset -90
        xanchor .5
    $ pause(0.1)
    show pluscredits_Altagram_portugese_t zorder 3 at pluscredits_name_left:
        yoffset -50
        xanchor .7
    show pluscredits_Altagram_portugese_n zorder 3 at pluscredits_name_left:
        yoffset -90
        xanchor .7
    $ pause(0.1)
    show pluscredits_Altagram_spanishLA_t zorder 3 at pluscredits_name_left:
        yoffset 40
        xanchor .3
    show pluscredits_Altagram_spanishLA_n zorder 3 at pluscredits_name_left:
        yoffset 0
        xanchor .3
    $ pause(0.1)
    show pluscredits_Altagram_spanishSP_t zorder 3 at pluscredits_name_left:
        yoffset 40
        xanchor .5
    show pluscredits_Altagram_spanishSP_n zorder 3 at pluscredits_name_left:
        yoffset 0
        xanchor .5
    $ pause(0.1)
    show pluscredits_Altagram_italian_t zorder 3 at pluscredits_name_left:
        yoffset 40
        xanchor .7
    show pluscredits_Altagram_italian_n zorder 3 at pluscredits_name_left:
        yoffset 0
        xanchor .7
    $ pause(0.1)
    show pluscredits_Altagram_japanese_t zorder 3 at pluscredits_name_left:
        yoffset 130
        xanchor .2
    show pluscredits_Altagram_japanese_n zorder 3 at pluscredits_name_left:
        yoffset 90
        xanchor .2
    $ pause(0.1)
    show pluscredits_Altagram_korean_t zorder 3 at pluscredits_name_left:
        yoffset 130
        xanchor .4
    show pluscredits_Altagram_korean_n zorder 3 at pluscredits_name_left:
        yoffset 90
        xanchor .4
    $ pause(0.1)
    show pluscredits_Altagram_chineseSM_t zorder 3 at pluscredits_name_left:
        yoffset 130
        xanchor .6
    show pluscredits_Altagram_chineseSM_n zorder 3 at pluscredits_name_left:
        yoffset 90
        xanchor .6
    $ pause(0.1)
    show pluscredits_Altagram_chineseTR_t zorder 3 at pluscredits_name_left:
        yoffset 130
        xanchor .8
    show pluscredits_Altagram_chineseTR_n zorder 3 at pluscredits_name_left:
        yoffset 90
        xanchor .8
    $ pause(0.1)
    show pluscredits_Altagram_project_manager_t zorder 3 at pluscredits_name_left:
        yoffset 220
        xanchor .3
    show pluscredits_Altagram_project_manager_n zorder 3 at pluscredits_name_left:
        yoffset 180
        xanchor .3
    $ pause(0.1)
    show pluscredits_Altagram_linguistic_lead_t zorder 3 at pluscredits_name_left:
        yoffset 220
        xanchor .5
    show pluscredits_Altagram_linguistic_lead_n zorder 3 at pluscredits_name_left:
        yoffset 180
        xanchor .5
    $ pause(0.1)
    show pluscredits_Altagram_partnership_manager_t zorder 3 at pluscredits_name_left:
        yoffset 220
        xanchor .7
    show pluscredits_Altagram_partnership_manager_n zorder 3 at pluscredits_name_left:
        yoffset 180
        xanchor .7
    $ pause(0.1)
    show pluscredits_Altagram_cco_t zorder 3 at pluscredits_name_left:
        yoffset 310
        xanchor .3
    show pluscredits_Altagram_cco_n zorder 3 at pluscredits_name_left:
        yoffset 270
        xanchor .3
    $ pause(0.1)
    show pluscredits_Altagram_coo_t zorder 3 at pluscredits_name_left:
        yoffset 310
        xanchor .5
    show pluscredits_Altagram_coo_n zorder 3 at pluscredits_name_left:
        yoffset 270
        xanchor .5
    $ pause(0.1)
    show pluscredits_Altagram_ceo_t zorder 3 at pluscredits_name_left:
        yoffset 310
        xanchor .7
    show pluscredits_Altagram_ceo_n zorder 3 at pluscredits_name_left:
        yoffset 270
        xanchor .7

    $ cgcount += 1
    $ pause(9.6)

    hide pluscredits_Fan_translation_support_title_t
    hide pluscredits_Fan_translation_simp_chinese_t
    hide pluscredits_Fan_translation_simp_chinese_n
    hide pluscredits_Fan_translation_trad_chinese_t
    hide pluscredits_Fan_translation_trad_chinese_n
    hide pluscredits_Fan_translation_japanese_t
    hide pluscredits_Fan_translation_japanese_n
    hide pluscredits_Creative_artists_agency_t
    hide pluscredits_Creative_artists_agency_n
    hide pluscredits_Special_thanks_l_t
    if renpy.mobile:
        hide pluscredits_Special_thanks_l_n_mobile
    else:
        hide pluscredits_Special_thanks_l_n
    hide pluscredits_Special_thanks_r_n

    hide pluscredits_cg
    hide pluscredits_name
    hide pluscredits_title
    show white at reveal_cg_right
    show pluscredits_cg12 as pluscredits_cg at pluscredits_left
    show pluscredits_End_thanks_t zorder 3 at pluscredits_final_thanks

    $ cgcount += 1
    $ pause(9.6 + 2.5)

    hide pluscredits_Altagram_title_t
    hide pluscredits_Altagram_production_title_t
    hide pluscredits_Altagram_production_PM_t
    hide pluscredits_Altagram_production_PM_n
    hide pluscredits_Altagram_production_SLE_t
    hide pluscredits_Altagram_production_SLE_n
    hide pluscredits_Altagram_production_LE_t
    hide pluscredits_Altagram_production_LE_n
    hide pluscredits_Altagram_french_t
    hide pluscredits_Altagram_french_n
    hide pluscredits_Altagram_german_t
    hide pluscredits_Altagram_german_n
    hide pluscredits_Altagram_portugese_t
    hide pluscredits_Altagram_portugese_n
    hide pluscredits_Altagram_spanishLA_t
    hide pluscredits_Altagram_spanishLA_n
    hide pluscredits_Altagram_spanishSP_t
    hide pluscredits_Altagram_spanishSP_n
    hide pluscredits_Altagram_italian_t
    hide pluscredits_Altagram_italian_n
    hide pluscredits_Altagram_japanese_t
    hide pluscredits_Altagram_japanese_n
    hide pluscredits_Altagram_korean_t
    hide pluscredits_Altagram_korean_n
    hide pluscredits_Altagram_chineseSM_t
    hide pluscredits_Altagram_chineseSM_n
    hide pluscredits_Altagram_chineseTR_t
    hide pluscredits_Altagram_chineseTR_n
    hide pluscredits_Altagram_project_manager_t
    hide pluscredits_Altagram_project_manager_n
    hide pluscredits_Altagram_linguistic_lead_t
    hide pluscredits_Altagram_linguistic_lead_n
    hide pluscredits_Altagram_partnership_manager_t
    hide pluscredits_Altagram_partnership_manager_n
    hide pluscredits_Altagram_cco_t
    hide pluscredits_Altagram_cco_n
    hide pluscredits_Altagram_coo_t
    hide pluscredits_Altagram_coo_n
    hide pluscredits_Altagram_ceo_t
    hide pluscredits_Altagram_ceo_n

    hide pluscredits_cg
    hide pluscredits_name
    hide pluscredits_title
    $ unlock("epilogue_cg")
    show white:
        xoffset 0
    show pluscredits_End_love_t zorder 3 at pluscredits_ts_transform:
        yoffset -140
    show pluscredits_ts_img zorder 3 at pluscredits_ts_transform
    $ pause(4)
    show white:
        xoffset 0
    $ pause(1)
    show pluscredits_sf_movie zorder 3 at pluscredits_ts_transform
    $ pause(4)
    show white:
        xoffset 0
    $ pause(1)
    show pluscredits_epilogue zorder 4
    $ pause(5)
    show black zorder 5:
        alpha 0
        linear 3 alpha 1
    stop music fadeout 3.5
    $ pause(3.5)
    jump desktop_from_side_stories
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
