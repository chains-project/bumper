```java
  @Test
    public void shouldPullPushedByTag() throws Exception {
        this.client.run("push", this.image.remote());
        this.client.run("image", "rm", this.image.name());
        this.client.run("image", "rm", this.image.remote());
        String output = this.client.run("pull", this.image.remote());
        assertThat(output, containsString("Status: Downloaded newer image for " + this.image.remote()));
    }
```