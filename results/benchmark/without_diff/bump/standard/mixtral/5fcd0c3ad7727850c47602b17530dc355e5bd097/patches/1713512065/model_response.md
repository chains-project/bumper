Here's a possible patch for the given client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

In this patch, I replaced the `getClassInfo` method with the `getClassInfoFor` method, which is a new method added in the `CoverageDatabase` class. The `getClassInfoFor` method takes a single argument of type `ClassName` and returns the class information for the given class name. In the original code, `getClassInfo` takes a set of `ClassName` objects and returns the class information for all of them. However, in this case, we only need the class information for a single class, which is represented by the `data.getMutatedClass()` expression. Therefore, we can use the `getClassInfoFor` method instead.