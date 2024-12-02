def basketball_shooting_simulation():
    print("Welcome to the Basketball Shooting Machine Simulation!")
    
    # Initialize counters
    total_shots = 0
    total_made = 0
    mid_range_shots = 0
    mid_range_made = 0
    three_pointer_shots = 0
    three_pointer_made = 0

    # Get the number of attempts
    try:
        attempts = int(input("Enter the number of attempts: "))
        if attempts <= 0:
            print("Number of attempts must be positive.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Loop through each attempt
    for i in range(1, attempts + 1):
        print(f"\nAttempt {i}:")
        shot_type = input("Enter shot type ('mid-range' or '3-pointer'): ").strip().lower()
        
        # Validate shot type
        if shot_type not in ['mid-range', '3-pointer']:
            print("Invalid shot type. Please enter 'mid-range' or '3-pointer'.")
            continue

        made = input("Did you make the shot? ('yes' or 'no'): ").strip().lower()
        if made not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue

        # Update counters
        total_shots += 1
        if shot_type == 'mid-range':
            mid_range_shots += 1
            if made == 'yes':
                mid_range_made += 1
                total_made += 1
        elif shot_type == '3-pointer':
            three_pointer_shots += 1
            if made == 'yes':
                three_pointer_made += 1
                total_made += 1

    # Calculate percentages
    total_percentage = (total_made / total_shots) * 100 if total_shots > 0 else 0
    mid_range_percentage = (mid_range_made / mid_range_shots) * 100 if mid_range_shots > 0 else 0
    three_pointer_percentage = (three_pointer_made / three_pointer_shots) * 100 if three_pointer_shots > 0 else 0

    # Display results
    print("\n--- Results ---")
    print(f"Total Shots Made: {total_made}/{total_shots} ({total_percentage:.2f}%)")
    print(f"Mid-Range Shots Made: {mid_range_made}/{mid_range_shots} ({mid_range_percentage:.2f}%)")
    print(f"3-Pointer Shots Made: {three_pointer_made}/{three_pointer_shots} ({three_pointer_percentage:.2f}%)")

# Run the simulation
basketball_shooting_simulation()
