```java
 @Test
    public void shouldPullPushedByTag() throws Exception {
        final String remote = this.image.remote();
        this.client.run("push", remote);
        this.client.run("image", "rm", this.image.name());
        this.client.run("image", "rm", remote);
        final String output = this.client.run("pull", remote);
        assertThat(output, containsString(String.format("Status: Downloaded newer image for %s", remote)));
    }
```