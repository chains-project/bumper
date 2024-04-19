Here is a fixed version of the method that should resolve the error:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

In the original code, the method `getClassInfo` was called on `coverage` with a `Set` of `ClassName`s as an argument. However, it seems that this method has been removed in the updated version of the library.

Instead, we can use the method `getClassInfoFor` which takes a single `ClassName` as an argument. This method should return the same information as the previous method, but in a slightly different format.

Therefore, in the fixed code, we call `getClassInfoFor` with `data.getMutatedClass()` as an argument, which should return the same information as `getClassInfo` with `java.util.Collections.singleton(data.getMutatedClass())` as an argument.