Since the package `org.jasypt.spring.security` does not exist, it seems that there was a change in the library version used. The class `PBEPasswordEncoder` might have been moved to a different package. 

A possible solution could be to import the class from its new package. For example, if the class was moved to the package `org.jasypt.springframework.security3`, the corrected import statement would be:

```java
import org.jasypt.springframework.security3.PBEPasswordEncoder;
```

Please replace the old import statement with the new one.