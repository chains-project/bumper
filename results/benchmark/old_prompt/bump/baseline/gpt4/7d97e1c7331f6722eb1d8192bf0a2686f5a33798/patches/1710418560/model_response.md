The error message indicates that the symbol `Tv` cannot be found. This could be because the `Tv` class is not present in the `com.jcabi.aspects` package anymore. 

Without knowing the exact context of the code, it's hard to provide a specific solution. However, if the `Tv` class has been moved to a different package, you should update the import statement to reflect the new package location. 

For instance, if `Tv` has been moved to the `com.jcabi.utils` package, you should change the import statement like this:

```java
import com.jcabi.utils.Tv;
```

If the `Tv` class has been removed completely, you'll need to find a replacement for it or implement the functionality it provided yourself. Unfortunately, without more information about what `Tv` does and what its replacement might be, I can't provide a more specific solution.