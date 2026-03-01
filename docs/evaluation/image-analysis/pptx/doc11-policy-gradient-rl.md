# Image Analysis: Doc 11 -- 11_policy_gradient_rl_lecture.pptx

**Document:** `11_policy_gradient_rl_lecture.pptx`
**Format:** PPTX
**Source:** https://www.cs.princeton.edu/courses/archive/spring17/cos598F/lectures/RL.pptx
**Category:** multi-image
**Images:** 14
**Document context:** Princeton COS 598F lecture slides on reinforcement learning
covering value-based methods (TD, Sarsa, Q-learning, DQN), policy gradient
methods (REINFORCE, actor-critic), and asynchronous algorithms (A3C).

<br><br>

## doc11-R01 -- Tabular TD(0) pseudocode

**Figure reference:** Slide 36
**Content type:** screenshot
**Annotation difficulty:** Medium
**Dimensions:** 784x307 pixels

### Visual Inventory [-> Completeness]

- **Image type:** Pseudocode algorithm box from a textbook (Sutton & Barto
  style)
- **Title line:** "Tabular TD(0) for estimating v_pi" in bold, dark gray
  header bar at top
- **Algorithm body (serif font, left-aligned, indented structure):**
  - "Input: the policy pi to be evaluated"
  - "Initialize V(s) arbitrarily (e.g., V(s) = 0, forall s in S+)"
  - "Repeat (for each episode):"
  - Indented: "Initialize S"
  - Indented: "Repeat (for each step of episode):"
  - Double-indented: "A <- action given by pi for S"
  - Double-indented: "Take action A, observe R, S'"
  - Double-indented: "V(S) <- V(S) + alpha[R + gamma V(S') - V(S)]"
  - Double-indented: "S <- S'"
  - Indented: "until S is terminal"
- **Formatting:**
  - Title bar: dark gray/charcoal background, bold white text
  - Body: white/light gray background with thin gray border
  - Variables in italics: V, s, S, S', A, R, pi
  - Greek letters: alpha, gamma, pi rendered in math notation
  - Mathematical symbols: forall, in, <-, +, -, *, []
  - Serif font (Computer Modern or similar LaTeX-typeset font)
- **No line numbers, no color coding, no annotations**

### Verifiable Facts [-> Accuracy]

- FACT: The title reads "Tabular TD(0) for estimating v_pi"
- FACT: The input is "the policy pi to be evaluated"
- FACT: V(s) is initialized arbitrarily with example V(s) = 0 for all s in S+
- FACT: The outer loop is "Repeat (for each episode)"
- FACT: The inner loop is "Repeat (for each step of episode)"
- FACT: The TD update rule is V(S) <- V(S) + alpha[R + gamma V(S') - V(S)]
- FACT: The termination condition is "until S is terminal"
- FACT: S <- S' updates the current state after each step
- FACT: The algorithm takes action A according to policy pi, not greedily

### Hallucination Risks [-> Accuracy]

- RISK: Adding a learning rate decay or step-size schedule
  REALITY: The algorithm uses a fixed alpha with no schedule mentioned
- RISK: Including an outer termination condition (number of episodes)
  REALITY: The outer "Repeat" has no explicit termination criterion shown
- RISK: Describing this as Q-learning or Sarsa
  REALITY: This is TD(0) for state-value estimation (V), not action-value
  (Q). It evaluates a fixed policy pi, does not learn a policy
- RISK: Claiming the image includes a convergence proof or guarantee
  REALITY: Only the algorithm pseudocode is shown, no theoretical analysis

### Detail Inventory [-> Specificity]

- Title bar: dark charcoal/gray (#404040 approximate), bold text
- Body: light gray background with thin border
- Font: serif (Computer Modern / LaTeX typesetting)
- Math symbols: alpha, gamma, pi, forall, in rendered as math glyphs
- Arrow notation: <- for assignment
- Indentation: 2 levels (episode loop, step loop)
- Variables: V(s), V(S), V(S'), S, S', A, R
- Parameters: alpha (step size), gamma (discount factor)
- Set notation: S+ (non-terminal states plus terminal)
- Image dimensions: 784x307 pixels, ~9.5x3.7 in at slide scale

### Domain Context [-> Usefulness]

This is the standard tabular TD(0) algorithm from Sutton and Barto's
"Reinforcement Learning: An Introduction." TD(0) (Temporal-Difference
learning with 0-step lookahead) is a model-free prediction algorithm
that estimates the state-value function V(s) under a given policy pi.

Key concepts:
- **TD update:** V(S) <- V(S) + alpha[R + gamma V(S') - V(S)]
  - alpha: learning rate (step size)
  - gamma: discount factor for future rewards
  - R + gamma V(S') - V(S): the TD error (delta)
- **Bootstrap:** Uses V(S') estimate rather than waiting for the full return
- **On-policy prediction:** Evaluates the value of following policy pi
- **v_pi:** The true state-value function under policy pi (what we estimate)

This appears on slide 36 of a Princeton COS 598F lecture on RL, in the
section covering temporal-difference methods.

### Search Keywords [-> Usefulness]

TD(0), temporal difference, tabular, state-value, V(s), policy evaluation,
reinforcement learning, Sutton Barto, pseudocode, alpha, gamma, TD error,
bootstrap, COS 598F, Princeton

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "An algorithm for reinforcement learning" (no specific algorithm name or update rule) | "Tabular TD(0) for estimating v_pi. Initializes V(s), loops over episodes and steps, updates V(S) <- V(S) + alpha[R + gamma V(S') - V(S)], terminates when S is terminal." | "Tabular TD(0) prediction algorithm. Input: policy pi. Init V(s)=0 forall s in S+. Nested loops: episodes (outer), steps (inner). Action A from pi, observe R, S'. TD update: V(S) <- V(S) + alpha[R + gamma V(S') - V(S)]. State transition S <- S'. Terminates on terminal state. On-policy evaluation, not control." |
| Specificity | "Pseudocode in a box" | "Dark header bar with title, serif font body, indented structure, math symbols (alpha, gamma, pi). LaTeX-style typesetting." | "Charcoal header bar (~#404040) with bold title. Light gray body with thin border. Computer Modern serif font. 2-level indentation. Math: alpha, gamma, pi, forall, in as glyphs. Arrow (<-) assignment. 784x307 px, ~9.5x3.7 in." |
| Completeness | "A TD algorithm" (misses initialization, loops, update rule details, termination) | "Title, input, initialization, outer/inner loops, action selection, observation, TD update, state transition, termination. All key elements covered." | "Every line of pseudocode transcribed: title, input (policy pi), init (V(s)=0, S+), episode loop, step loop, action (A from pi for S), observe (R, S'), update (V(S) with TD), transition (S<-S'), termination (S terminal). Formatting: header bar, body, indentation, math notation. No color, no line numbers." |
| Usefulness | "A reinforcement learning algorithm from a lecture" | "Standard TD(0) from Sutton & Barto. On-policy prediction using temporal-difference learning. From Princeton COS 598F RL lecture." | "Sutton & Barto's tabular TD(0) prediction algorithm. Estimates V(s) under fixed pi via bootstrapped TD error delta = R + gamma V(S') - V(S). On-policy (evaluates pi, no control). Slide 36 of Princeton COS 598F, value-based methods section. Foundation for Sarsa, Q-learning, DQN." |

<br><br>

## doc11-R04 -- DQN loss function and gradient

**Figure reference:** Slide 48
**Content type:** screenshot
**Annotation difficulty:** Hard
**Dimensions:** 699x356 pixels

### Visual Inventory [-> Completeness]

- **Image type:** Screenshot of academic paper text (from Mnih et al. 2015,
  the DQN Nature paper) showing the loss function definition and gradient
  derivation
- **Content structure:** Two paragraphs of prose text with two numbered
  equations
- **Paragraph 1 (top):** Introduces the Q-network concept and loss function
  - Defines Q-network as neural network function approximator with weights
    theta
  - States the loss function L_i(theta_i) changes at each iteration i
- **Equation (2):**
  - L_i(theta_i) = E_{s,a~rho(.)} [(y_i - Q(s, a; theta_i))^2]
  - Centered, numbered "(2)" at right margin
- **Paragraph 2 (middle):** Defines the target y_i and explains behavior
  distribution
  - y_i = E_{s'~E} [r + gamma max_{a'} Q(s', a'; theta_{i-1}) | s, a]
  - Defines rho(s,a) as the behaviour distribution
  - Notes theta_{i-1} parameters are held fixed during optimization
  - Compares to supervised learning (targets depend on network weights)
- **Equation (3):**
  - Gradient: nabla_{theta_i} L_i(theta_i) = E_{s,a~rho(.);s'~E}
    [(r + gamma max_{a'} Q(s', a'; theta_{i-1}) - Q(s, a; theta_i))
    nabla_{theta_i} Q(s, a; theta_i)]
  - Centered, numbered "(3)" at right margin
- **Paragraph 3 (bottom):** Discusses stochastic gradient descent
  approximation, mentions single samples replacing expectations, references
  "the familiar Q-learning algorithm [26]"
- **Formatting:** LaTeX-typeset academic paper text, serif font (Computer
  Modern), justified alignment, standard mathematical notation with
  subscripts, superscripts, Greek letters
- **No figures, diagrams, or color** -- purely text and equations

### Verifiable Facts [-> Accuracy]

- FACT: Equation (2) defines L_i(theta_i) as the expected squared difference
  between y_i and Q(s, a; theta_i)
- FACT: The target y_i uses theta_{i-1} (previous iteration parameters), not
  theta_i
- FACT: The max operation in y_i is over a' (next actions)
- FACT: rho(s,a) is called the "behaviour distribution"
- FACT: Equation (3) is the gradient of L_i with respect to theta_i
- FACT: The gradient includes nabla_{theta_i} Q(s, a; theta_i) at the end
- FACT: The text references "[26]" as the Q-learning algorithm citation
- FACT: The text explicitly states "the targets depend on the network weights"
- FACT: Equations are numbered (2) and (3)

### Hallucination Risks [-> Accuracy]

- RISK: Confusing theta_i with theta_{i-1} in the target
  REALITY: The target y_i explicitly uses theta_{i-1} (fixed parameters from
  previous iteration), which is a key design choice in DQN
- RISK: Describing the experience replay mechanism
  REALITY: Experience replay is mentioned in the surrounding paper context
  but this specific excerpt focuses on the loss function and gradient. The
  emulator E is referenced but the replay buffer is not shown here
- RISK: Adding equations not present in the image (e.g., the Bellman equation)
  REALITY: Only equations (2) and (3) are shown
- RISK: Identifying the exact paper without the title being visible
  REALITY: The content is recognizably from Mnih et al. 2015 (DQN Nature
  paper) but the paper title and author names are not visible in this crop

### Detail Inventory [-> Specificity]

- Font: Computer Modern serif (LaTeX), justified paragraphs
- Equations: centered, numbered at right margin in parentheses
- Subscripts: theta_i, theta_{i-1}, L_i, y_i, a', s'
- Greek letters: theta, rho, gamma, nabla
- Operators: E (expectation), max, nabla (gradient)
- Special notation: rho(.) for behavior distribution, E for emulator
- Equation numbering: (2) and (3)
- Citation reference: [26] for Q-learning
- Text terms in bold/italics: "behaviour distribution" emphasized
- Image dimensions: 699x356 px, ~9.4x4.8 in at slide scale
- Black text on white background, no color

### Domain Context [-> Usefulness]

This is from the landmark DQN paper (Mnih et al., "Human-level control
through deep reinforcement learning," Nature, 2015). The excerpt defines
the core optimization objective of DQN:

- **Loss function (Eq. 2):** Mean squared error between the target y_i and
  the Q-network prediction Q(s, a; theta_i). The target uses theta_{i-1}
  (frozen parameters) to stabilize training.
- **Gradient (Eq. 3):** The gradient of the loss, used for SGD updates. In
  practice, single-sample stochastic gradients replace the full expectations.
- **Key innovation:** Using fixed target parameters theta_{i-1} rather than
  the current theta_i. This breaks the correlation between targets and
  predictions that destabilizes naive Q-learning with function approximation.
- **Behaviour distribution rho:** The policy used to collect data (e.g.,
  epsilon-greedy), which may differ from the greedy policy being learned
  (off-policy).

The bottom paragraph connects this to standard Q-learning by noting that
SGD with single samples recovers the familiar Q-learning update.

### Search Keywords [-> Usefulness]

DQN, Deep Q-Network, loss function, gradient, Q-learning, Mnih, Nature
2015, behaviour distribution, target network, theta, neural network,
function approximation, reinforcement learning, experience replay, SGD

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "Mathematical equations from a paper" (no algorithm identification, no equation content) | "DQN loss function from Mnih et al. Eq (2): L_i = E[(y_i - Q(s,a;theta_i))^2]. Eq (3): gradient with target using theta_{i-1}. Target y_i uses max_{a'} Q(s',a';theta_{i-1})." | "DQN paper excerpt with 2 equations: (2) L_i(theta_i) = E_{s,a~rho}[(y_i - Q(s,a;theta_i))^2], where y_i = E[r + gamma max_{a'} Q(s',a';theta_{i-1})|s,a]. (3) gradient nabla_{theta_i} L_i includes TD error times nabla Q. Key: theta_{i-1} fixed in target (not theta_i). rho = behaviour distribution. Connects to Q-learning [26] via SGD." |
| Specificity | "Equations with Greek letters" | "Computer Modern font, LaTeX typeset, equations numbered (2) and (3), subscript notation for iterations (i, i-1), citation [26]." | "LaTeX Computer Modern serif, justified text. Centered equations numbered (2)/(3) at right margin. Subscripts: theta_i, theta_{i-1}. Greek: theta, rho, gamma, nabla. E for expectation, E for emulator. 'Behaviour distribution' in emphasis. 699x356 px, ~9.4x4.8 in." |
| Completeness | "DQN loss function" (misses gradient, target definition, behavior distribution, SGD connection) | "Loss function (2), gradient (3), target y_i definition with theta_{i-1}, behaviour distribution rho, SGD simplification to Q-learning." | "All content: intro paragraph (Q-network, loss sequence), Eq (2) (MSE loss), target definition (y_i with theta_{i-1}, max_{a'}, E), behaviour distribution rho(s,a), theta_{i-1} fixed explanation, contrast with supervised learning, Eq (3) (full gradient), SGD paragraph with [26] reference." |
| Usefulness | "Part of a reinforcement learning paper" | "Core DQN optimization from Mnih et al. 2015 Nature paper. Defines loss and gradient that enable stable Q-learning with deep neural networks. Target network (theta_{i-1}) is the key stabilization mechanism." | "Mnih et al. 2015 DQN: loss Eq(2) and gradient Eq(3). Innovation: frozen target theta_{i-1} breaks target-prediction correlation. Behaviour distribution rho enables off-policy learning. SGD approximation recovers tabular Q-learning. Foundation for all deep RL value methods. Slide 48 of Princeton COS 598F." |

<br><br>

## doc11-R05 -- Deep Q-learning with Experience Replay

**Figure reference:** Slide 49
**Content type:** screenshot
**Annotation difficulty:** Hard
**Dimensions:** 717x362 pixels

### Visual Inventory [-> Completeness]

- **Image type:** Full algorithm pseudocode box from a paper (Mnih et al.
  2015, DQN Nature paper)
- **Title line:** "Algorithm 1 Deep Q-learning with Experience Replay" in
  bold, with horizontal rule below
- **Algorithm structure (LaTeX typeset, serif font, indented):**
  - "Initialize replay memory D to capacity N"
  - "Initialize action-value function Q with random weights"
  - "for episode = 1, M do"
  - Indented: "Initialise sequence s_1 = {x_1} and preprocessed sequenced
    phi_1 = phi(s_1)"
  - Indented: "for t = 1, T do"
  - Double-indented block:
    - "With probability epsilon select a random action a_t"
    - "otherwise select a_t = max_a Q*(phi(s_t), a; theta)"
    - "Execute action a_t in emulator and observe reward r_t and image x_{t+1}"
    - "Set s_{t+1} = s_t, a_t, x_{t+1} and preprocess phi_{t+1} = phi(s_{t+1})"
    - "Store transition (phi_t, a_t, r_t, phi_{t+1}) in D"
    - "Sample random minibatch of transitions (phi_j, a_j, r_j, phi_{j+1})
      from D"
    - "Set y_j = { r_j for terminal phi_{j+1} ; r_j + gamma max_{a'}
      Q(phi_{j+1}, a'; theta) for non-terminal phi_{j+1} }" (piecewise
      definition with curly brace)
    - "Perform a gradient descent step on (y_j - Q(phi_j, a_j; theta))^2
      according to equation 3"
  - "end for"
  - "end for"
- **Formatting:**
  - Bold title "Algorithm 1" followed by algorithm name
  - Serif font (Computer Modern), LaTeX typeset
  - Standard algorithm environment with "for...do...end for" structure
  - Mathematical variables in italics: D, N, Q, s, x, phi, a, r, theta,
    epsilon, gamma
  - Subscripts: t, t+1, j, j+1, 1
  - Piecewise y_j definition uses curly brace notation
  - Reference to "equation 3" (with a small red box around "3" -- appears
    to be a hyperlink artifact)
- **No color coding** (except the red box around reference "3")
- **Black text on white background**

### Verifiable Facts [-> Accuracy]

- FACT: Title reads "Algorithm 1 Deep Q-learning with Experience Replay"
- FACT: Replay memory D is initialized to capacity N
- FACT: Q is initialized with random weights
- FACT: Outer loop runs for M episodes
- FACT: Inner loop runs for T time steps per episode
- FACT: Action selection uses epsilon-greedy: random with probability epsilon,
  otherwise greedy a_t = max_a Q*(phi(s_t), a; theta)
- FACT: Transitions (phi_t, a_t, r_t, phi_{t+1}) are stored in D
- FACT: A random minibatch is sampled from D for each update
- FACT: Target y_j has a piecewise definition: r_j for terminal, r_j + gamma
  max_{a'} Q(phi_{j+1}, a'; theta) for non-terminal
- FACT: Gradient descent uses (y_j - Q(phi_j, a_j; theta))^2 as the loss
- FACT: The gradient step references "equation 3"
- FACT: Preprocessing function phi is applied to sequences

### Hallucination Risks [-> Accuracy]

- RISK: Describing a target network (separate theta^- parameters)
  REALITY: This version of the algorithm uses theta for both the Q-network
  and the target computation. The target network with separate frozen
  parameters (theta^-) is a later refinement not shown in this Algorithm 1
- RISK: Including frame skipping or action repeat
  REALITY: These implementation details are discussed elsewhere in the paper
  but not in this algorithm box
- RISK: Describing the preprocessing function phi in detail
  REALITY: phi(s_t) is referenced but not defined in this box. The paper
  defines it elsewhere (typically last 4 frames, grayscale, downsampled)
- RISK: Stating the minibatch size
  REALITY: No specific minibatch size is given in the algorithm

### Detail Inventory [-> Specificity]

- Algorithm label: "Algorithm 1" in bold
- Font: Computer Modern serif (LaTeX)
- Horizontal rule below title
- Loop keywords: "for...do", "end for" (2 nested levels)
- Variable notation: italic letters with subscripts
- Greek letters: epsilon, phi, gamma, theta
- Piecewise brace: curly brace for y_j definition (2 cases)
- Reference: "equation 3" with red hyperlink box artifact around "3"
- Indentation: 3 levels (base, episode, timestep)
- Black text on white background
- Image dimensions: 717x362 px, ~9.6x4.8 in

### Domain Context [-> Usefulness]

This is Algorithm 1 from Mnih et al. 2015 (the DQN Nature paper), the
complete Deep Q-learning with Experience Replay algorithm. Key components:

- **Experience replay (D):** Stores transitions and samples random
  minibatches, breaking temporal correlations in training data
- **Epsilon-greedy exploration:** Balances exploration (random actions with
  probability epsilon) and exploitation (greedy Q-value maximization)
- **Preprocessing phi:** Converts raw game frames to fixed-size input
  representations for the neural network
- **Piecewise target:** Terminal states get reward only (r_j); non-terminal
  states get reward plus discounted max future Q-value

This is one of the most cited algorithms in deep RL, demonstrating
human-level Atari game playing. It appears on slide 49 of the Princeton
COS 598F lecture.

### Search Keywords [-> Usefulness]

DQN, Deep Q-learning, experience replay, algorithm, pseudocode, Mnih,
Nature 2015, epsilon-greedy, replay memory, minibatch, target, gradient
descent, Atari, reinforcement learning, COS 598F

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A reinforcement learning algorithm" (no name, no key steps) | "Algorithm 1: Deep Q-learning with Experience Replay. Epsilon-greedy action selection, store transitions in replay memory D, sample minibatch, compute target y_j (terminal/non-terminal), gradient descent on squared error." | "Full DQN algorithm: init D(capacity N), init Q(random). M episodes, T steps each. Epsilon-greedy: random or a_t=max_a Q*(phi(s_t),a;theta). Store (phi_t,a_t,r_t,phi_{t+1}) in D. Sample minibatch. y_j = r_j (terminal) or r_j + gamma max_{a'} Q(phi_{j+1},a';theta) (non-terminal). GD on (y_j-Q(phi_j,a_j;theta))^2 per eq 3. No separate target network in this version." |
| Specificity | "Pseudocode with math notation" | "LaTeX Computer Modern font, Algorithm 1 label, bold title, 2 nested for-do-end loops, piecewise y_j with curly brace, reference to equation 3." | "Bold 'Algorithm 1' + name. Horizontal rule. Computer Modern serif. 3-level indentation. for episode=1,M / for t=1,T structure. Piecewise curly brace for y_j. Red hyperlink box around '3' reference. Greek: epsilon, phi, gamma, theta. 717x362 px." |
| Completeness | "DQN algorithm box" (misses initialization, replay, target, gradient steps) | "Initialization (D, Q), episode/step loops, epsilon-greedy, emulator execution, replay storage, minibatch sampling, target computation, gradient step. All major steps covered." | "Every line: init D to N, init Q random, for episodes, init s_1/phi_1, for steps, epsilon-greedy, execute/observe, set s_{t+1}/phi_{t+1}, store transition, sample minibatch, piecewise y_j, GD step per eq 3. Both end-for. Title, formatting, reference artifact noted." |
| Usefulness | "A deep learning algorithm from a paper" | "Complete DQN algorithm from Mnih et al. 2015. Key innovations: experience replay buffer, epsilon-greedy exploration, minibatch SGD. Foundation of deep RL for Atari games." | "Mnih et al. 2015 Algorithm 1. Experience replay breaks temporal correlation. Epsilon-greedy balances exploration/exploitation. Minibatch SGD from replay buffer D. Note: this version uses single theta (no target network theta^-). Preprocessing phi converts frames. Piecewise target handles terminal/non-terminal. Princeton COS 598F slide 49." |

<br><br>

## doc11-R10 -- A3C actor-critic pseudocode

**Figure reference:** Slide 79
**Content type:** screenshot
**Annotation difficulty:** Hard
**Dimensions:** 803x482 pixels

### Visual Inventory [-> Completeness]

- **Image type:** Full algorithm pseudocode box from a paper (Mnih et al.
  2016, A3C paper)
- **Title line:** "Algorithm S3 Asynchronous advantage actor-critic -
  pseudocode for each actor-learner thread." in bold, with horizontal rule
  below
- **Algorithm structure (LaTeX typeset, serif font, indented):**
  - Comments (italic, prefixed with //):
    - "// Assume global shared parameter vectors theta and theta_v, and
      global shared counter T = 0"
    - "// Assume thread-specific parameter vectors theta' and theta'_v"
  - "Initialize thread step counter t <- 1"
  - "repeat"
  - Indented block:
    - "Reset gradients: d_theta <- 0 and d_theta_v <- 0."
    - "Synchronize thread-specific parameters theta' = theta and
      theta'_v = theta_v"
    - "t_start = t"
    - "Get state s_t"
    - Inner "repeat" loop:
      - "Perform a_t according to policy pi(a_t | s_t; theta')"
      - "Receive reward r_t and new state s_{t+1}"
      - "t <- t + 1"
      - "T <- T + 1"
    - "until terminal s_t or t - t_start == t_max"
    - Piecewise R definition with curly brace:
      - "R = { 0 for terminal s_t ; V(s_t, theta'_v) for non-terminal
        s_t // Bootstrap from last state }"
    - "for i in {t-1, ..., t_start} do"
    - Indented:
      - "R <- r_i + gamma R"
      - "Accumulate gradients wrt theta': d_theta <- d_theta +
        nabla_{theta'} log pi(a_i | s_i; theta')(R - V(s_i; theta'_v))"
      - "Accumulate gradients wrt theta'_v: d_theta_v <- d_theta_v +
        partial (R - V(s_i; theta'_v))^2 / partial theta_v"
    - "end for"
    - "Perform asynchronous update of theta using d_theta and of theta_v
      using d_theta_v."
  - "until T > T_max"
- **Formatting:**
  - Bold "Algorithm S3" label with full title
  - Horizontal rule separating title from body
  - Serif font (Computer Modern), LaTeX typeset
  - Italic comments with // prefix
  - Standard algorithm environment with repeat-until and for-do-end for
  - Mathematical variables: theta, theta_v, theta', theta'_v, pi, gamma,
    nabla, partial
  - Subscripts: t, t+1, i, start, max, v
  - Piecewise curly brace for R
- **Black text on white background, no color**

### Verifiable Facts [-> Accuracy]

- FACT: Title reads "Algorithm S3 Asynchronous advantage actor-critic"
- FACT: There are two sets of parameters: global (theta, theta_v) and
  thread-specific (theta', theta'_v)
- FACT: T is a global shared counter initialized to 0
- FACT: Thread parameters are synchronized from global at start of each
  iteration
- FACT: Actions are selected by policy pi(a_t | s_t; theta')
- FACT: The inner loop runs until terminal state or t - t_start == t_max
- FACT: R is bootstrapped from V(s_t, theta'_v) for non-terminal states
- FACT: R is 0 for terminal states
- FACT: Gradient accumulation loop runs backwards: i in {t-1, ..., t_start}
- FACT: R is computed as r_i + gamma R (discounted return, accumulated
  backwards)
- FACT: Policy gradient uses log pi(a_i | s_i; theta') * (R - V(s_i;
  theta'_v)) as the advantage
- FACT: Value gradient uses partial (R - V(s_i; theta'_v))^2 / partial
  theta_v
- FACT: Asynchronous update pushes d_theta and d_theta_v to global parameters
- FACT: Outer loop terminates when T > T_max

### Hallucination Risks [-> Accuracy]

- RISK: Confusing A3C with A2C (synchronous version)
  REALITY: This is explicitly "Asynchronous" -- each thread independently
  updates global parameters without synchronization barriers
- RISK: Describing entropy regularization
  REALITY: No entropy term is shown in this algorithm box. The full A3C
  paper includes entropy regularization but it is not in this pseudocode
- RISK: Stating the number of parallel threads
  REALITY: The algorithm describes "each actor-learner thread" but does not
  specify how many threads run in parallel
- RISK: Confusing the supplementary algorithm number (S3) with Algorithm 3
  REALITY: The label is "S3" (supplementary), not "3" from the main paper

### Detail Inventory [-> Specificity]

- Algorithm label: "Algorithm S3" in bold (supplementary material)
- Full title includes "pseudocode for each actor-learner thread"
- Comment syntax: italic text with // prefix
- Two parameter sets: global (theta, theta_v) and thread-local (theta',
  theta'_v)
- Counter variables: t (thread step), T (global step), t_start, t_max, T_max
- Loop structures: outer repeat-until (T > T_max), inner repeat-until
  (terminal or t_max steps), for-do-end for (backward accumulation)
- Piecewise R with curly brace (2 cases: terminal/non-terminal)
- Comment "// Bootstrap from last state" on the non-terminal case
- Gradient notation: nabla for policy gradient, partial for value gradient
- Advantage: R - V(s_i; theta'_v) appears in both gradient lines
- Serif font (Computer Modern), LaTeX, black on white
- Image dimensions: 803x482 px, ~9.5x5.7 in

### Domain Context [-> Usefulness]

This is Algorithm S3 from the A3C paper (Mnih et al., "Asynchronous Methods
for Deep Reinforcement Learning," ICML 2016). A3C (Asynchronous Advantage
Actor-Critic) was a breakthrough in deep RL that replaced experience replay
with parallelism:

- **Asynchronous:** Multiple actor-learner threads run independently, each
  interacting with its own copy of the environment
- **Advantage:** Uses R - V(s) as the advantage estimate, reducing variance
  compared to raw returns
- **Actor-Critic:** Separate policy (theta/theta') and value (theta_v/
  theta'_v) parameter sets, updated simultaneously
- **n-step returns:** The inner loop collects up to t_max steps before
  computing returns and gradients (n-step TD rather than 1-step)
- **Global update:** Thread-local gradients are pushed asynchronously to
  shared global parameters

This appears on slide 79 of the Princeton COS 598F lecture, in the section
on asynchronous deep RL methods.

### Search Keywords [-> Usefulness]

A3C, asynchronous advantage actor-critic, algorithm, pseudocode, Mnih,
ICML 2016, policy gradient, value function, advantage, n-step return,
parallel threads, global parameters, reinforcement learning, COS 598F

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A reinforcement learning algorithm with Greek symbols" | "A3C Algorithm S3: each thread synchronizes params, collects t_max steps, computes n-step returns R backwards, accumulates policy and value gradients, pushes async update to global params theta/theta_v." | "Algorithm S3 (A3C) per-thread pseudocode. Global: theta, theta_v, T=0. Thread: theta', theta'_v. Sync theta'=theta. Inner loop: pi(a_t|s_t;theta') until terminal or t-t_start==t_max. R=0 (terminal) or V(s_t,theta'_v) (bootstrap). Backward i=t-1..t_start: R=r_i+gamma*R. Policy grad: nabla log pi * (R-V). Value grad: partial (R-V)^2. Async push d_theta, d_theta_v. Until T>T_max." |
| Specificity | "Algorithm box with math formulas" | "Bold 'Algorithm S3' label. Computer Modern font, LaTeX. Two repeat-until loops + one for-do loop. Piecewise R. // comments for parameter assumptions. nabla and partial operators." | "Bold 'Algorithm S3' with full title. Horizontal rule. 2 italic // comments. 3 loop levels: repeat-until (T>T_max), repeat-until (terminal or t_max), for-do-end for (backward). Piecewise curly brace with '// Bootstrap' comment. nabla_{theta'} for policy, partial/partial theta_v for value. 803x482 px." |
| Completeness | "Actor-critic algorithm" (misses initialization, sync, gradient details, termination) | "Parameter init (global/thread), sync step, action selection, reward collection, R computation (terminal/non-terminal), backward gradient accumulation (policy + value), async global update, termination condition." | "Every line: // comments on params, init t=1, repeat, reset grads, sync theta'/theta'_v, t_start, get state, inner repeat (action, reward, t++, T++), until terminal/t_max, piecewise R, backward for-loop (R=r_i+gamma*R, policy grad, value grad), end for, async update, until T>T_max. Title, label, all notation." |
| Usefulness | "A deep RL paper algorithm" | "A3C per-thread pseudocode from Mnih et al. 2016. Replaces experience replay with parallel threads. Advantage R-V reduces variance. N-step returns via t_max." | "Mnih et al. ICML 2016 Algorithm S3 (supplementary). A3C: multiple threads async update global theta/theta_v. No replay buffer needed. n-step advantage: R-V(s;theta'_v). Backward return computation. Policy gradient: nabla log pi * advantage. Value: MSE gradient. Key innovation: parallelism stabilizes training without replay. Princeton COS 598F slide 79." |

<br><br>

## doc11-R11 -- Softmax policy parameterization

**Figure reference:** Slide 55
**Content type:** equation
**Annotation difficulty:** Easy
**Dimensions:** 246x70 pixels

### Visual Inventory [-> Completeness]

- **Image type:** Single mathematical equation, standalone
- **Equation:**
  pi(a | s, theta) = exp(h(s, a, theta)) / sum_b exp(h(s, b, theta))
- **Left side:** pi(a | s, theta) -- the policy probability of action a given
  state s and parameters theta
- **Right side:** Softmax fraction:
  - Numerator: exp(h(s, a, theta))
  - Denominator: sum_b exp(h(s, b, theta))
  - Horizontal fraction bar separating numerator and denominator
- **Variables:**
  - pi: policy function (italic)
  - a: action (italic)
  - s: state (italic)
  - theta: parameter vector (italic)
  - h: preference function (italic)
  - b: summation index over actions (italic, subscript on sum)
  - exp: exponential function (roman/upright)
- **Formatting:** LaTeX-typeset, serif font (Computer Modern), black text on
  white background
- **No equation number, no surrounding text, no box or border**

### Verifiable Facts [-> Accuracy]

- FACT: The equation defines pi(a | s, theta) as a softmax over h(s, a,
  theta)
- FACT: The numerator is exp(h(s, a, theta))
- FACT: The denominator sums exp(h(s, b, theta)) over all actions b
- FACT: The summation index is b (not a')
- FACT: h takes three arguments: s, a (or b), and theta
- FACT: The conditioning bar separates a from s and theta on the left side

### Hallucination Risks [-> Accuracy]

- RISK: Defining h(s, a, theta) as a specific function (e.g., linear
  theta^T phi(s,a))
  REALITY: The equation only shows h as an unspecified preference function.
  No definition of h is given in this image.
- RISK: Adding a temperature parameter tau to the softmax
  REALITY: No temperature parameter is shown. The standard softmax is used
  without temperature scaling.
- RISK: Stating this is the Boltzmann distribution
  REALITY: While structurally identical to the Boltzmann distribution, the
  image uses the term "softmax" implicitly through its standard form. No
  name is given in the image itself.

### Detail Inventory [-> Specificity]

- Equation layout: fraction with horizontal bar
- Font: Computer Modern serif (LaTeX)
- Greek: pi, theta (italic)
- Roman: exp (upright)
- Summation: sum_b with lowercase b as index
- Conditioning: vertical bar | in pi(a | s, theta)
- Arguments separated by commas: (s, a, theta) and (s, b, theta)
- Small image: 246x70 px, ~3.4x1.0 in at slide scale
- No equation number or label
- Clean rendering, high contrast

### Domain Context [-> Usefulness]

This is the softmax (or Gibbs) policy parameterization, a standard approach
in policy gradient methods. It maps a preference function h(s, a, theta) to
action probabilities:

- **h(s, a, theta):** A learned preference or score for taking action a in
  state s, parameterized by theta. In the simplest case, h = theta^T phi(s,a)
  (linear in features), but can also be a neural network output.
- **Softmax normalization:** Ensures pi(a | s, theta) is a valid probability
  distribution: all values in [0,1] and sum to 1 over actions.
- **Differentiable:** The softmax is smooth and differentiable with respect
  to theta, enabling gradient-based policy optimization (REINFORCE,
  actor-critic).

This appears on slide 55 of the Princeton COS 598F lecture, in the section
on policy gradient methods, before the REINFORCE algorithm.

### Search Keywords [-> Usefulness]

softmax policy, policy parameterization, pi(a|s,theta), preference function,
Gibbs distribution, policy gradient, reinforcement learning, action
probability, exponential, COS 598F

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A mathematical formula with exp" (no identification of softmax or policy) | "Softmax policy: pi(a|s,theta) = exp(h(s,a,theta)) / sum_b exp(h(s,b,theta)). Maps preferences h to action probabilities." | "pi(a|s,theta) = exp(h(s,a,theta)) / sum_b exp(h(s,b,theta)). Softmax over preference function h. Numerator: exp of action a's preference. Denominator: sum over all actions b. No temperature parameter. h is unspecified (not defined here). Summation index is b, not a'." |
| Specificity | "An equation with Greek letters" | "LaTeX Computer Modern, fraction layout, italic variables (pi, theta, a, s, h, b), upright exp, summation sum_b." | "246x70 px (~3.4x1.0 in). Computer Modern serif. Fraction bar. Italic: pi, a, s, theta, h, b. Roman: exp. Conditioning bar in pi(a|s,theta). Comma-separated args. sum_b subscript. No equation number. No border or surrounding text." |
| Completeness | "Softmax equation" (misses variable identification, argument structure) | "LHS: pi(a|s,theta). RHS: exp fraction with h function. Variables: pi (policy), a (action), s (state), theta (params), h (preference), b (sum index)." | "LHS pi(a|s,theta) with conditioning bar. RHS fraction: numerator exp(h(s,a,theta)), denominator sum_b exp(h(s,b,theta)). All variables identified. No temperature, no equation number, no h definition. Standalone equation, no text context." |
| Usefulness | "A formula from a lecture" | "Standard softmax policy parameterization from policy gradient RL. Maps preference scores to valid probability distribution over actions." | "Softmax/Gibbs policy parameterization: h(s,a,theta) -> pi(a|s,theta). Foundation for REINFORCE and actor-critic. Differentiable wrt theta for gradient-based optimization. h can be linear (theta^T phi) or neural net. Slide 55 of Princeton COS 598F, policy gradient section." |

<br><br>

## doc11-R13 -- Actor-critic update with baseline

**Figure reference:** Slide 62
**Content type:** equation
**Annotation difficulty:** Medium
**Dimensions:** 567x131 pixels

### Visual Inventory [-> Completeness]

- **Image type:** Two-line mathematical equation showing the actor-critic
  policy parameter update rule
- **Line 1:**
  theta_{t+1} .= theta_t + alpha (G_t^{(1)} - v_hat(S_t, w))
  * nabla_theta pi(A_t | S_t, theta) / pi(A_t | S_t, theta)
- **Line 2 (continuation, aligned with = sign):**
  = theta_t + alpha (R_{t+1} + gamma v_hat(S_{t+1}, w) - v_hat(S_t, w))
  * nabla_theta pi(A_t | S_t, theta) / pi(A_t | S_t, theta)
- **The ".=" notation:** A dot above the equals sign on line 1 indicates
  "approximately equal" or "defined as proportional to"
- **Key components:**
  - theta_{t+1}: updated policy parameters
  - theta_t: current policy parameters
  - alpha: step size / learning rate
  - G_t^{(1)}: one-step return (superscript (1) in parentheses)
  - v_hat(S_t, w): value function estimate with weight vector w
  - R_{t+1}: reward at next step
  - gamma: discount factor
  - v_hat(S_{t+1}, w): next-state value estimate
  - nabla_theta pi(A_t | S_t, theta) / pi(A_t | S_t, theta): the score
    function (gradient of log policy)
- **Formatting:** LaTeX-typeset, serif font (Computer Modern), black text on
  white background. Two lines aligned on the equals sign. Fraction bar for
  the score function ratio.
- **No equation number, no surrounding text**

### Verifiable Facts [-> Accuracy]

- FACT: The equation has two lines, with the second expanding G_t^{(1)}
- FACT: G_t^{(1)} = R_{t+1} + gamma v_hat(S_{t+1}, w) (one-step return)
- FACT: The baseline subtracted is v_hat(S_t, w)
- FACT: The advantage term is G_t^{(1)} - v_hat(S_t, w) = R_{t+1} + gamma
  v_hat(S_{t+1}, w) - v_hat(S_t, w), which is the TD error delta
- FACT: The score function is written as nabla_theta pi / pi (equivalent to
  nabla_theta log pi)
- FACT: The value function uses weight vector w (separate from policy theta)
- FACT: A dot appears above the first equals sign (.=)
- FACT: Uppercase letters S_t, A_t, R_{t+1} denote random variables
- FACT: v_hat has a hat accent (estimated value, not true value)

### Hallucination Risks [-> Accuracy]

- RISK: Calling this the REINFORCE update
  REALITY: This is specifically the actor-critic update (one-step return with
  baseline), not pure REINFORCE (which uses the full return G_t, not
  bootstrapped)
- RISK: Omitting the hat on v_hat
  REALITY: v_hat (with hat) denotes the estimated value function, distinct
  from the true value v_pi. The hat is visually small but present.
- RISK: Misreading G_t^{(1)} as G_t^1 or G_t'
  REALITY: The superscript is "(1)" in parentheses, denoting the 1-step
  return specifically
- RISK: Stating that the .= means strict equality
  REALITY: The dot above = indicates an approximate or proportional
  relationship, acknowledging that the update is a stochastic approximation

### Detail Inventory [-> Specificity]

- Two-line equation aligned on = sign
- Line 1: theta_{t+1} .= ... with dot-equals notation
- Line 2: = theta_t + alpha(...) with expanded G_t^{(1)}
- Score function as fraction: nabla_theta pi(A_t|S_t,theta) over
  pi(A_t|S_t,theta) with horizontal fraction bar
- Subscripts: t, t+1
- Superscript: (1) in parentheses on G_t
- Greek: theta, alpha, gamma, pi, nabla
- Hat accent: v_hat (estimated value function)
- Weight vectors: theta (policy), w (value)
- Font: Computer Modern serif (LaTeX)
- Image: 567x131 px, ~7.9x1.8 in
- Black on white, no color, no border

### Domain Context [-> Usefulness]

This is the one-step actor-critic update rule from Sutton and Barto's
"Reinforcement Learning: An Introduction." It combines:

- **Actor update (policy):** theta adjusted in the direction of the score
  function nabla log pi, weighted by the advantage
- **Critic baseline:** v_hat(S_t, w) subtracted from the return to reduce
  variance while keeping the gradient unbiased
- **TD error as advantage:** The second line reveals that
  G_t^{(1)} - v_hat(S_t, w) = R_{t+1} + gamma v_hat(S_{t+1}, w) -
  v_hat(S_t, w) = delta_t, the one-step TD error

Key insight: using the TD error delta as the advantage estimate allows
the actor to update after every step (online), rather than waiting for
episode completion (like REINFORCE). This is the foundation for modern
actor-critic methods including A2C/A3C.

This appears on slide 62 of the Princeton COS 598F lecture, bridging
REINFORCE and actor-critic methods.

### Search Keywords [-> Usefulness]

actor-critic, policy gradient, baseline, advantage, TD error, one-step
return, score function, nabla log pi, value function, theta update,
reinforcement learning, Sutton Barto, COS 598F

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Accuracy | "A mathematical equation with theta and pi" | "Actor-critic update: theta_{t+1} = theta_t + alpha * (one-step advantage) * score function. Line 2 expands advantage as TD error: R_{t+1} + gamma v_hat(S_{t+1}) - v_hat(S_t)." | "Two-line aligned equation. Line 1: theta_{t+1} .= theta_t + alpha(G_t^{(1)} - v_hat(S_t,w)) * nabla_theta pi / pi. Line 2 expands G_t^{(1)} = R_{t+1} + gamma v_hat(S_{t+1},w). Advantage = TD error delta_t. .= denotes approximate. v_hat has hat accent. Separate params: theta (policy), w (value)." |
| Specificity | "Equations with subscripts" | "Two lines aligned on =. LaTeX Computer Modern. Score function as fraction. Dot-equals on line 1. Superscript (1) on G_t. Hat accent on v." | "567x131 px (~7.9x1.8 in). Computer Modern serif. Aligned =. Dot above first =. G_t^{(1)} with parenthesized superscript. v_hat with hat accent. Fraction bar for nabla pi/pi. Greek: theta, alpha, gamma, pi, nabla. Uppercase random vars S_t, A_t, R_{t+1}. No equation number." |
| Completeness | "Policy update equation" (misses baseline, TD error, score function details) | "Both lines of equation. Key terms: G_t^{(1)}, v_hat baseline, score function nabla pi/pi, expansion to TD error. Separate theta and w." | "Both lines fully transcribed. All variables: theta_{t+1}, theta_t, alpha, G_t^{(1)}, v_hat(S_t,w), R_{t+1}, gamma, v_hat(S_{t+1},w), nabla_theta, pi(A_t|S_t,theta). Dot-equals notation. Hat accent. Fraction form of score function. Line 2 shows G_t^{(1)} expansion. No surrounding text." |
| Usefulness | "An RL update equation from a lecture" | "One-step actor-critic update from Sutton & Barto. Uses TD error as advantage estimate. Enables online (per-step) policy updates unlike REINFORCE." | "Sutton & Barto one-step actor-critic. G_t^{(1)} - v_hat = delta_t (TD error) as advantage. Score function nabla log pi weighted by delta. Baseline v_hat(S_t,w) reduces variance. Foundation for A2C/A3C. Separate params: theta (actor/policy), w (critic/value). Slide 62 of COS 598F, bridging REINFORCE to actor-critic." |
