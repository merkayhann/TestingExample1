from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import selectors
from Elements.elements import *
from goodreads_functions import *
from test_login import *
import datetime


@pytest.mark.header
def test_searchbar_on_header():
    test_login_with_valid_credentials()
    click_element(inputBox_searchBox_onHeader)
    type_input(inputBox_searchBox_onHeader,input_bookName)
    click_element(btn_searchBox_onHeader)
    assert get_text_value(lbl_searchOnSearchResultsPage) == 'Search'
    assert get_text_value(link_booksOnSearchResultsPage) == 'Book'
 
@pytest.mark.header2
def test_myBooks_on_header():
    test_login_with_valid_credentials()
    click_element(link_myBooks_onHeader)
    assert get_content(txt_myBooks_pageTitle)=="Meryem Kayhan’s books on Goodreads (0 books)"
    assert get_text_value(link_myBooks_onMyBooksPage)=="My Books"
    
@pytest.mark.header3
def test_browse_on_header():
    test_login_with_valid_credentials()
    click_element(dd_browse_onHeader)
    click_element(dd_browse_sublink_recommendations)
    assert get_text_value(lbl_recommendations_onRecommendationsPage)=="Recommendations"
    click_element(dd_browse_onHeader)
    click_element(dd_browse_sublink_choiceAwards)
    assert get_text_value(lbl_choiceChatters_onChoiceAwardsPage)=="CHOICE CHATTER"
    click_element(dd_browse_onHeader)
    click_element(dd_browse_sublink_giveaways)
    assert get_text_value(lbl_giveaways_onGiveawaysPage)=="Giveaways"
    click_element(link_home_onHeader2)
    click_element(dd_browse_onHeader)
    click_element(dd_browse_sublink_newReleases)
    assert get_text_value(link_myAuthors_onNewReleasesPage)=="My authors"
    click_element(dd_browse_onHeader)
    click_element(dd_browse_sublink_lists)
    assert get_text_value(lbl_listopia_onListsPage)=="Listopia"
    click_element(dd_browse_onHeader)
    click_element(dd_browse_sublink_explore)
    assert get_text_value(lbl_trending_onExplorePage)=="Trending with Goodreads members"
    click_element(link_home_onHeader2)
    click_element(dd_browse_onHeader)
    click_element(dd_browse_sublink_newsAndInterviews)
    assert get_text_value(lbl_newsAndInterviews_onNewsAndInterviewsPage)=="News and Interviews"   
    click_element(dd_browse_onHeader)
    genreName=get_text_value(dd_browse_sublink_fantasy)
    click_element(dd_browse_sublink_fantasy)
    assert get_text_value(lbl_genreName_onGenresPage)==genreName
    click_element(dd_browse_onHeader)
    genreName=get_text_value(dd_browse_sublink_fiction)
    click_element(dd_browse_sublink_fiction)
    assert get_text_value(lbl_genreName_onGenresPage)==genreName
    click_element(dd_browse_onHeader)
    genreName=get_text_value(dd_browse_sublink_historicalFiction)
    click_element(dd_browse_sublink_historicalFiction)
    assert get_text_value(lbl_genreName_onGenresPage)==genreName
    click_element(dd_browse_onHeader)
    genreName=get_text_value(dd_browse_sublink_scienceFiction)
    click_element(dd_browse_sublink_scienceFiction)
    assert get_text_value(lbl_genreName_onGenresPage)==genreName
    click_element(dd_browse_onHeader)
    genreName=get_text_value(dd_browse_sublink_allGenres)
    click_element(dd_browse_sublink_allGenres)
    assert get_text_value(lbl_genre_onGenresPage)=="Genres"
    
@pytest.mark.header4
def test_community_on_header():
    test_login_with_valid_credentials()
    click_element(dd_community_onHeader)
    click_element(dd_community_sublink_quotes)
    assert get_text_value(lbl_popularQuotes_onPopularQuotesPage)=="Popular quotes"   

@pytest.mark.header5
def test_logo_and_home_on_header():
    test_login_with_valid_credentials()
    click_element(link_myBooks_onHeader)
    assert get_text_value(link_myBooks_onMyBooksPage)=="My Books"
    click_element(img_logo_onHeader)
    assert get_text_value(lbl_currentlyReading_onMainpageLeftSidebar)=="CURRENTLY READING"
    click_element(dd_community_onHeader)
    click_element(dd_community_sublink_quotes)
    assert get_text_value(lbl_popularQuotes_onPopularQuotesPage)=="Popular quotes"   
    click_element(link_home_onHeader)
    assert get_text_value(lbl_newsAndInterviews_onMainpageRightSidebar)=="NEWS & INTERVIEWS"

