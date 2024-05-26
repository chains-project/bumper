```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    // create a string that indicates the layer already exists
    String layerAlreadyExists = String.format("%s: Layer already exists", this.image.layer());

    // return a matcher that checks if the string contains the layer already exists message
    return new org.hamcrest.core.StringContains(layerAlreadyExists);
}
```