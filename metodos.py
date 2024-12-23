find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")


def findById( self, elem_id ):
        return self.driver.find_element_by_id( elem_id )

def findAllByClass( self, class_name ):
        return self.driver.find_elements( By.CLASS_NAME, class_name )

def findAllByName( self, name ):
        return self.driver.find_elements( By.NAME, name )

def findAllByTagName( self, name ):
        return self.driver.find_elements_by_tag_name( name )
def findByLinkText( self, text ):
        return self.driver.find_element_by_link_text( text )