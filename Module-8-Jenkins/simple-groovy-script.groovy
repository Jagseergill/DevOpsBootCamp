def buildApp(){
    echo 'Building the Application'
}

def testApp(){
    echo 'Testing the application'
}


def deployApp(){
    echo 'Deploying the application.'
    echo "Deplying version ${VERSION}"
}

return this
