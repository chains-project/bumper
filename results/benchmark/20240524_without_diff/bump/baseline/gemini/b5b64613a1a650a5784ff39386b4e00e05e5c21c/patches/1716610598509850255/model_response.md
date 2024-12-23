```java
  public void prepare() {

    PerforceScm perforceScm = getJenkinsScm();
    String credentials = perforceScm.getCredential();

    IOptionsServer server = ConnectionFactory.getConnection();
    try {
      String clientString = getClientString();
      if (new ConnectionHelper(credentials, buildListener).isClient(clientString)) {
        ClientHelper perforceClient = new ClientHelper(credentials, buildListener, clientString, StandardCharsets.UTF_8.toString());
        IClient client = perforceClient.getClient();
        try {
          this.perforce = new PerforceClient(server, client);
          this.perforce.initConnection();
        } catch (Exception e) {
          logger.warning("Could not instantiate connection with PerforceClient: " + e.getMessage());
        }
      } else {
        logger.warning("Client " + clientString + " is not a valid client.");
      }
    } catch (Exception e) {
      logger.log(Level.FINE, "Error occurred: ", e);
    }

  }
```