Here's a possible patch to fix the error:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    // Create a new ClassInfoBuilder instance
    org.pitest.classinfo.ClassInfoBuilder classInfoBuilder = new org.pitest.classinfo.ClassInfoBuilder(data.getMutatedClass());
    // Get the ClassInfo object using the ClassInfoBuilder
    org.pitest.classinfo.ClassInfo classInfo = classInfoBuilder.build();
    // Create a new MutationTestSummaryData instance
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
This patch creates a new `ClassInfoBuilder` instance using the `data.getMutatedClass()` method, and then uses the `build()` method of the `ClassInfoBuilder` to get a `ClassInfo` object. The `ClassInfo` object is then passed to the `MutationTestSummaryData` constructor, along with the `data.getFileName()` and `data.getMutations()` methods.


This patch should fix the error because it uses the `org.pitest.classinfo.ClassInfoBuilder` class, which is available in the new library version, to get a `ClassInfo` object. The `getClassInfo()` method of the `CoverageDatabase` class is not needed, as the `ClassInfoBuilder` class provides a way to create a `ClassInfo` object directly from a `ClassName` object.