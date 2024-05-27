Here is a possible patch for the failing client code:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(),
            org.pitest.classinfo.ClassInfoFactory.forName(data.getMutatedClass()).getClassFile());
}
```
In this patch, we use the new `ClassInfoFactory` class to create a `ClassInfo` object for the mutated class, instead of using the deprecated `getClassInfo` method of `CoverageDatabase`. We then extract the class file from the `ClassInfo` object to pass it to the `MutationTestSummaryData` constructor.

Note that this patch assumes that the `data.getMutatedClass()` method returns a `String` object representing the fully qualified name of the mutated class. If this is not the case, the patch may need to be adjusted accordingly.