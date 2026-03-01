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

### Visual Inventory [-> Information Recovery]

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

### Verifiable Facts [-> Correctness]

- FACT: The title reads "Tabular TD(0) for estimating v_pi"
- FACT: The input is "the policy pi to be evaluated"
- FACT: V(s) is initialized arbitrarily with example V(s) = 0 for all s in S+
- FACT: The outer loop is "Repeat (for each episode)"
- FACT: The inner loop is "Repeat (for each step of episode)"
- FACT: The TD update rule is V(S) <- V(S) + alpha[R + gamma V(S') - V(S)]
- FACT: The termination condition is "until S is terminal"
- FACT: S <- S' updates the current state after each step
- FACT: The algorithm takes action A according to policy pi, not greedily

### Hallucination Risks [-> Correctness]

- RISK: Adding a learning rate decay or step-size schedule
  REALITY: The algorithm uses a fixed alpha with no schedule mentioned
- RISK: Including an outer termination condition (number of episodes)
  REALITY: The outer "Repeat" has no explicit termination criterion shown
- RISK: Describing this as Q-learning or Sarsa
  REALITY: This is TD(0) for state-value estimation (V), not action-value
  (Q). It evaluates a fixed policy pi, does not learn a policy
- RISK: Claiming the image includes a convergence proof or guarantee
  REALITY: Only the algorithm pseudocode is shown, no theoretical analysis

### Detail Inventory [-> Information Recovery]

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

### Domain Context [-> Retrieval Value]

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

### Search Keywords [-> Retrieval Value]

TD(0), temporal difference, tabular, state-value, V(s), policy evaluation,
reinforcement learning, Sutton Barto, pseudocode, alpha, gamma, TD error,
bootstrap, COS 598F, Princeton

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "An algorithm for reinforcement learning" -- no algorithm name, no update rule, no mathematical symbols. Or: transcribes the update rule with wrong symbols (e.g., replacing gamma with lambda, or using Q(s,a) instead of V(S)). Misidentifying this as Q-learning or SARSA triggers the hallucination cap -- this is TD(0) prediction (state-value V, not action-value Q). Getting the nesting wrong (e.g., describing one loop instead of two nested loops) is a structural error. | Tabular TD(0) for estimating v_pi identified. Initialization, nested loops, TD update rule V(S) <- V(S) + alpha[R + gamma V(S') - V(S)] correctly transcribed. Terminates when S is terminal. May miss the "forall s in S+" detail in initialization or the exact input line wording. | Every line of pseudocode exact: title "Tabular TD(0) for estimating v_pi", input (policy pi), init (V(s) = 0, forall s in S+), nested loops (episodes outer, steps inner), A from pi for S, observe R and S', TD update with alpha/gamma/V(S')/V(S) terms correct, S <- S', until S is terminal. No symbol substitutions. On-policy prediction correctly distinguished from control. |
| Information Recovery | Identifies as an RL algorithm in a box. A search for "TD(0)" or "V(S) + alpha" or "temporal difference" would not match. The algorithm name, update rule, loop structure, and mathematical notation are invisible. | Title, input, initialization, loop structure, update rule, and termination all recovered. "Tabular TD(0) prediction" would match. May miss the 2-level indentation structure, the charcoal header bar, the Computer Modern serif font, or the exact mathematical glyph rendering (alpha, gamma, pi as symbols). | Complete recovery: title text, every pseudocode line with correct indentation level, all mathematical symbols (alpha, gamma, pi, forall, in, arrow assignment). Formatting noted: charcoal header bar, light gray body, thin border, serif font, 2-level indentation. No line numbers, no color in body. Any symbol or pseudocode line visible in the image is findable -- parity principle met. |
| Retrieval Value | "A reinforcement learning algorithm from a lecture" -- no algorithm name, not self-contained. Would not surface for "TD(0) prediction" or "temporal difference update rule" or "Sutton and Barto pseudocode." | "Standard TD(0) from Sutton & Barto for on-policy prediction via temporal-difference learning." Searchable but doesn't explain bootstrapping or the TD error concept. | Natural prose identifying this as Sutton & Barto's tabular TD(0) prediction algorithm. Explains: estimates V(s) under fixed pi via bootstrapped TD error (R + gamma V(S') - V(S)). On-policy evaluation only (not control). From Princeton COS 598F policy gradient RL lecture (slide 36, value-based methods section). Foundation algorithm leading to SARSA, Q-learning, and DQN. Domain vocabulary embedded (TD(0), temporal difference, bootstrapping, on-policy prediction, value function). Self-contained. Findable by "tabular TD(0) pseudocode" or "temporal difference prediction algorithm." |

<br><br>

## doc11-R04 -- DQN loss function and gradient

**Figure reference:** Slide 48
**Content type:** screenshot
**Annotation difficulty:** Hard
**Dimensions:** 699x356 pixels

### Visual Inventory [-> Information Recovery]

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

### Verifiable Facts [-> Correctness]

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

### Hallucination Risks [-> Correctness]

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

### Detail Inventory [-> Information Recovery]

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

### Domain Context [-> Retrieval Value]

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

### Search Keywords [-> Retrieval Value]

DQN, Deep Q-Network, loss function, gradient, Q-learning, Mnih, Nature
2015, behaviour distribution, target network, theta, neural network,
function approximation, reinforcement learning, experience replay, SGD

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "Mathematical equations from a paper" -- no algorithm name, no equation content, no symbols transcribed. Or: transcribes the loss function with theta_i in the target instead of theta_{i-1} (the frozen target is the key innovation -- getting this wrong fundamentally mischaracterizes DQN). Substituting V for Q or omitting the max_{a'} operator misrepresents the algorithm type (this is action-value, not state-value). Fabricating equation numbers not shown (e.g., adding an "Eq (1)") triggers the hallucination cap. | DQN loss function identified: Eq (2) with MSE loss and Eq (3) with gradient. Target y_i uses theta_{i-1} (frozen) and max_{a'} Q(s',a';theta_{i-1}). Behaviour distribution rho mentioned. Connection to Q-learning via SGD. May miss the exact subscript notation or the "emulator E" distinction. | Both equations transcribed exactly: (2) L_i(theta_i) = E_{s,a~rho}[(y_i - Q(s,a;theta_i))^2] with target y_i = E[r + gamma max_{a'} Q(s',a';theta_{i-1})|s,a]; (3) gradient with nabla_{theta_i} and TD error. Key detail: theta_{i-1} is fixed (not theta_i) in the target. rho = behaviour distribution. Citation [26] connects to Q-learning. No symbol substitutions or fabricated equation numbers. |
| Information Recovery | Identifies as mathematical equations. A search for "DQN loss function" or "theta_{i-1}" or "behaviour distribution" would not match. The equation structure, frozen target mechanism, and Q-learning connection are invisible. | Both equations numbered and transcribed, target definition with theta_{i-1} noted, behaviour distribution rho described, SGD connection to Q-learning mentioned. "DQN loss gradient" would match. May miss the expectation subscript notation, the emphasized "behaviour distribution" text, or the supervised learning contrast paragraph. | Complete recovery: intro paragraph (Q-network, loss sequence), Eq (2) fully transcribed (MSE loss with rho subscript), target definition (y_i with theta_{i-1}, max_{a'}, conditional expectation), behaviour distribution rho(s,a) explanation, theta_{i-1} fixed vs theta_i contrast with supervised learning, Eq (3) fully transcribed (gradient with TD error), SGD paragraph with [26] citation. LaTeX Computer Modern serif font, equation numbering at right margin. Any equation, variable, or paragraph visible in the excerpt is findable -- parity principle met. |
| Retrieval Value | "Part of a reinforcement learning paper" -- no paper name, not self-contained. Would not surface for "DQN loss function" or "target network stabilization" or "Mnih et al. 2015." | "Core DQN optimization from Mnih et al. 2015 Nature paper defining loss and gradient with frozen target network." Searchable but doesn't explain why the frozen target matters. | Natural prose identifying this as the DQN loss and gradient from Mnih et al. 2015 Nature paper. Explains the key innovation: frozen target parameters theta_{i-1} break the destabilizing target-prediction correlation that prevented earlier neural Q-learning. Behaviour distribution rho enables off-policy learning from replay buffer. SGD approximation recovers tabular Q-learning as a special case [26]. Foundation for all subsequent deep RL value methods (Double DQN, Dueling, Rainbow). From Princeton COS 598F slide 48. Domain vocabulary embedded (DQN, target network, behaviour distribution, SGD, off-policy). Self-contained. Findable by "DQN loss function gradient" or "Mnih target network stabilization." |

<br><br>

## doc11-R05 -- Deep Q-learning with Experience Replay

**Figure reference:** Slide 49
**Content type:** screenshot
**Annotation difficulty:** Hard
**Dimensions:** 717x362 pixels

### Visual Inventory [-> Information Recovery]

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

### Verifiable Facts [-> Correctness]

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

### Hallucination Risks [-> Correctness]

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

### Detail Inventory [-> Information Recovery]

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

### Domain Context [-> Retrieval Value]

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

### Search Keywords [-> Retrieval Value]

DQN, Deep Q-learning, experience replay, algorithm, pseudocode, Mnih,
Nature 2015, epsilon-greedy, replay memory, minibatch, target, gradient
descent, Atari, reinforcement learning, COS 598F

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A reinforcement learning algorithm" -- no algorithm name, no key innovation identified. Or: claims this includes a separate target network theta^- (this version uses single theta -- the target network variant came later). Transcribing the piecewise y_j incorrectly (e.g., swapping terminal/non-terminal conditions) is a structural error. Fabricating additional algorithm steps not shown or inventing hyperparameter values triggers the hallucination cap. Misidentifying as policy gradient (this is value-based DQN) is a category error. | Algorithm 1: Deep Q-learning with Experience Replay identified. Key steps correct: epsilon-greedy, replay memory D, minibatch sampling, piecewise y_j (terminal/non-terminal), gradient descent per equation 3. Nested for loops (M episodes, T steps). May miss the preprocessing phi function, the exact initialization lines, or the single-theta detail. | Full algorithm transcribed: init D(capacity N), init Q(random weights). for episode=1,M: init s_1={x_1}, phi_1=phi(s_1). for t=1,T: epsilon-greedy (random or a_t=max_a Q*(phi(s_t),a;theta)). Execute, observe r_t, x_{t+1}. Set s_{t+1}, phi_{t+1}. Store (phi_t,a_t,r_t,phi_{t+1}) in D. Sample minibatch. Piecewise y_j: r_j (terminal phi_{j+1}) or r_j + gamma max_{a'} Q(phi_{j+1},a';theta) (non-terminal). GD on (y_j - Q(phi_j,a_j;theta))^2 per eq 3. Single theta (no separate target network). No fabricated steps. |
| Information Recovery | Identifies as a reinforcement learning pseudocode box. A search for "Deep Q-learning" or "Experience Replay" or "epsilon-greedy" would not match. The algorithm name, replay mechanism, target computation, and gradient step are invisible. | Algorithm name, initialization, loop structure, epsilon-greedy, replay storage/sampling, piecewise target, and gradient step all recovered. "DQN experience replay algorithm" would match. May miss the preprocessing phi notation, the red hyperlink artifact on equation reference "3", or the exact s_{t+1}/phi_{t+1} transition notation. | Complete recovery: "Algorithm 1" label and title, every pseudocode line with correct 3-level indentation, all mathematical symbols (epsilon, phi, gamma, theta, D, N, M, T), piecewise y_j with curly brace and terminal/non-terminal conditions, equation 3 reference with red hyperlink artifact. Bold title, horizontal rule, Computer Modern serif font. Both end-for markers. Any line, variable, or notation visible in the algorithm is findable -- parity principle met. |
| Retrieval Value | "A deep learning algorithm from a paper" -- no paper name, not self-contained. Would not surface for "DQN algorithm" or "experience replay" or "Mnih et al. 2015." | "Complete DQN algorithm from Mnih et al. 2015 with experience replay buffer and epsilon-greedy exploration." Searchable but doesn't explain why replay matters or the single-theta limitation. | Natural prose identifying this as Algorithm 1 from Mnih et al. 2015 Nature DQN paper. Explains experience replay (breaks temporal correlation in training samples), epsilon-greedy (balances exploration/exploitation), minibatch SGD from replay buffer D. Notes this version uses single theta (no separate target network theta^- as in later improvements). Preprocessing phi converts raw frames. Piecewise target handles episode termination. Princeton COS 598F slide 49. Domain vocabulary embedded (DQN, experience replay, epsilon-greedy, minibatch SGD, temporal correlation). Self-contained. Findable by "DQN experience replay algorithm" or "Deep Q-learning pseudocode." |

<br><br>

## doc11-R10 -- A3C actor-critic pseudocode

**Figure reference:** Slide 79
**Content type:** screenshot
**Annotation difficulty:** Hard
**Dimensions:** 803x482 pixels

### Visual Inventory [-> Information Recovery]

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

### Verifiable Facts [-> Correctness]

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

### Hallucination Risks [-> Correctness]

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

### Detail Inventory [-> Information Recovery]

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

### Domain Context [-> Retrieval Value]

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

### Search Keywords [-> Retrieval Value]

A3C, asynchronous advantage actor-critic, algorithm, pseudocode, Mnih,
ICML 2016, policy gradient, value function, advantage, n-step return,
parallel threads, global parameters, reinforcement learning, COS 598F

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A reinforcement learning algorithm with Greek symbols" -- no algorithm name, no key mechanism identified. Or: confuses this with DQN or describes it as value-based only (A3C is actor-critic with both policy and value gradients). Misrepresenting the gradient accumulation (e.g., omitting the backward computation direction from t-1 to t_start) is a structural error. Fabricating hyperparameter values (e.g., "learning rate = 0.001") not shown triggers the hallucination cap. | A3C Algorithm S3 identified: thread sync, t_max step collection, n-step return R, backward gradient accumulation (policy + value), async global update. Global theta/theta_v and thread theta'/theta'_v distinction noted. Piecewise R (terminal vs bootstrap). May miss the "// Bootstrap" comment or the T>T_max outer termination. | Full algorithm transcribed: "Algorithm S3 Asynchronous advantage actor-critic" title. Global: theta, theta_v, T=0. Thread: theta', theta'_v. Init t=1. Outer repeat: reset grads, sync theta'=theta/theta'_v=theta_v. Inner repeat: pi(a_t|s_t;theta'), receive r_t, t++, T++. Until terminal or t-t_start==t_max. Piecewise R: 0 (terminal) or V(s_t,theta'_v) with "// Bootstrap" comment. Backward for i=t-1..t_start: R=r_i+gamma*R, policy grad (nabla log pi * (R-V)), value grad (partial (R-V)^2). Async push. Until T>T_max. No fabricated hyperparameters. |
| Information Recovery | Identifies as an algorithm box with math. A search for "A3C" or "asynchronous advantage" or "actor-critic thread" would not match. The algorithm name, dual gradient mechanism, and async update architecture are invisible. | Algorithm label, parameter initialization, sync mechanism, loop structure, piecewise R, backward gradient computation, and async update all recovered. "A3C actor-critic pseudocode" would match. May miss the "// Assume" comment text, the exact backward loop range notation, or the nabla_{theta'} vs partial/partial theta_v operator distinction. | Complete recovery: "Algorithm S3" label with full title, 2 italic // comments, init t=1, 3 nested loop levels (outer repeat-until T>T_max, inner repeat-until terminal/t_max, backward for-do-end). Piecewise R with curly brace and "// Bootstrap" comment. Both gradient accumulation lines with distinct operators (nabla for policy, partial for value). Async update line. Bold title, horizontal rule, Computer Modern font. Any pseudocode line or notation visible is findable -- parity principle met. |
| Retrieval Value | "A deep RL paper algorithm" -- no paper name, not self-contained. Would not surface for "A3C pseudocode" or "asynchronous advantage actor-critic" or "parallel thread gradient." | "A3C per-thread pseudocode from Mnih et al. 2016 replacing experience replay with parallel threads." Searchable but doesn't explain the advantage mechanism or why parallelism helps. | Natural prose identifying this as Algorithm S3 from Mnih et al. ICML 2016 (supplementary material). A3C: asynchronous advantage actor-critic using multiple parallel threads instead of replay buffer. Each thread collects n-step rollouts, computes advantage R-V(s;theta'_v) for variance reduction, accumulates both policy (nabla log pi) and value (MSE) gradients, then pushes asynchronous updates to global parameters. Key innovation: parallelism provides diverse training samples, stabilizing training without replay. Princeton COS 598F slide 79. Domain vocabulary embedded (A3C, actor-critic, advantage, n-step return, async gradient). Self-contained. Findable by "A3C actor-critic algorithm" or "asynchronous advantage pseudocode." |

<br><br>

## doc11-R11 -- Softmax policy parameterization

**Figure reference:** Slide 55
**Content type:** equation
**Annotation difficulty:** Easy
**Dimensions:** 246x70 pixels

### Visual Inventory [-> Information Recovery]

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

### Verifiable Facts [-> Correctness]

- FACT: The equation defines pi(a | s, theta) as a softmax over h(s, a,
  theta)
- FACT: The numerator is exp(h(s, a, theta))
- FACT: The denominator sums exp(h(s, b, theta)) over all actions b
- FACT: The summation index is b (not a')
- FACT: h takes three arguments: s, a (or b), and theta
- FACT: The conditioning bar separates a from s and theta on the left side

### Hallucination Risks [-> Correctness]

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

### Detail Inventory [-> Information Recovery]

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

### Domain Context [-> Retrieval Value]

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

### Search Keywords [-> Retrieval Value]

softmax policy, policy parameterization, pi(a|s,theta), preference function,
Gibbs distribution, policy gradient, reinforcement learning, action
probability, exponential, COS 598F

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A mathematical formula with exp" -- no identification of softmax or policy. Or: transcribes the summation index as a' instead of b (the image clearly shows sum_b). Including a temperature parameter tau that is not shown triggers the hallucination cap. Misidentifying pi as a constant (3.14...) rather than a policy function is a symbol error. Describing h as a specific function (e.g., "linear in theta") when h is left unspecified in the equation is a domain knowledge fabrication. | Softmax policy equation identified: pi(a|s,theta) = exp(h(s,a,theta)) / sum_b exp(h(s,b,theta)). Numerator and denominator structure correct. No temperature parameter. May miss the italic vs roman font distinction or note that h is unspecified. | Exact transcription: pi(a|s,theta) = exp(h(s,a,theta)) / sum_b exp(h(s,b,theta)). Numerator: exp of action a's preference. Denominator: sum over all actions b (not a'). h is unspecified (not defined in this image). No temperature parameter. Conditioning bar in pi(a|s,theta). Summation index b correctly identified. Standalone equation with no equation number, no border, no surrounding text. No fabricated parameters or function definitions. |
| Information Recovery | Identifies as a math formula with exp. A search for "softmax policy" or "pi(a|s,theta)" or "preference function h" would not match. The policy parameterization, variable roles, and softmax normalization are invisible. | LHS and RHS transcribed, all variables identified (pi, a, s, theta, h, b), softmax structure recognized. "Softmax policy parameterization" would match. May miss the standalone nature (no context), the absence of equation number, or the font style details. | Complete recovery: LHS pi(a|s,theta) with conditioning bar and comma-separated arguments. RHS fraction with numerator exp(h(s,a,theta)) and denominator sum_b exp(h(s,b,theta)). All variables identified with roles. No equation number, no border, no surrounding text. Computer Modern serif font, italic variables, roman exp. Standalone equation. Any symbol or structural element visible is findable -- parity principle met. |
| Retrieval Value | "A formula from a lecture" -- no concept name, not self-contained. Would not surface for "softmax policy" or "Gibbs policy parameterization" or "policy gradient foundation." | "Softmax policy parameterization mapping preference scores to action probabilities." Searchable but doesn't explain why this matters for policy gradient methods. | Natural prose identifying this as the softmax (Gibbs) policy parameterization: h(s,a,theta) maps to pi(a|s,theta) via normalized exponentials, producing a valid probability distribution over actions. Foundation for REINFORCE and actor-critic methods -- differentiable with respect to theta for gradient-based optimization. h can be linear (theta^T phi) or neural network. Slide 55 of Princeton COS 598F policy gradient section. Domain vocabulary embedded (softmax policy, preference function, policy parameterization, REINFORCE, differentiable). Self-contained. Findable by "softmax policy parameterization" or "action probability exp normalization." |

<br><br>

## doc11-R13 -- Actor-critic update with baseline

**Figure reference:** Slide 62
**Content type:** equation
**Annotation difficulty:** Medium
**Dimensions:** 567x131 pixels

### Visual Inventory [-> Information Recovery]

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

### Verifiable Facts [-> Correctness]

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

### Hallucination Risks [-> Correctness]

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

### Detail Inventory [-> Information Recovery]

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

### Domain Context [-> Retrieval Value]

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

### Search Keywords [-> Retrieval Value]

actor-critic, policy gradient, baseline, advantage, TD error, one-step
return, score function, nabla log pi, value function, theta update,
reinforcement learning, Sutton Barto, COS 598F

### Annotation Quality Anchors

| Dimension | 40 (poor) | 70 (adequate) | 95 (excellent) |
|-----------|-----------|---------------|-----------------|
| Correctness | "A mathematical equation with theta and pi" -- no algorithm identification, no distinction between actor and critic parameters. Or: omits the hat accent on v (v_hat is a function approximator, not the true value function -- this distinction matters). Transcribing the .= (dot-equals, approximate equality) as plain = changes the mathematical meaning. Swapping theta and w roles (e.g., claiming w parameterizes the policy) is a structural error. Fabricating an equation number not shown triggers the hallucination cap. | Actor-critic update identified: theta_{t+1} = theta_t + alpha * advantage * score function. Line 2 expands G_t^{(1)} as R_{t+1} + gamma v_hat(S_{t+1},w) - v_hat(S_t,w). Separate parameters theta (policy) and w (value). May miss the dot-equals notation or the hat accent significance. | Two-line aligned equation exact. Line 1: theta_{t+1} .= theta_t + alpha(G_t^{(1)} - v_hat(S_t,w)) * nabla_theta pi(A_t|S_t,theta) / pi(A_t|S_t,theta). Line 2 expands: G_t^{(1)} = R_{t+1} + gamma v_hat(S_{t+1},w). Dot-equals (.=) for approximate equality. v_hat with hat accent (approximator, not true V). Separate parameters: theta (policy/actor), w (value/critic). Score function as fraction nabla pi / pi. No equation number, no surrounding text. No fabricated terms or simplified notation. |
| Information Recovery | Identifies as an RL equation with Greek symbols. A search for "actor-critic update" or "TD error advantage" or "score function" would not match. The two-parameter structure, advantage formulation, and score function fraction are invisible. | Both lines transcribed, G_t^{(1)} expansion shown, separate theta/w noted, score function fraction described. "Actor-critic policy gradient update" would match. May miss the dot-equals vs equals distinction, the hat accent on v, the uppercase convention for random variables (S_t, A_t, R_{t+1}), or the parenthesized superscript (1) on G. | Complete recovery: both lines fully transcribed with all variables (theta_{t+1}, theta_t, alpha, G_t^{(1)}, v_hat with hat, S_t, A_t, R_{t+1}, gamma, w, nabla_theta, pi). Dot-equals notation. Hat accent. Fraction form of score function. Line alignment. G_t^{(1)} expansion on line 2. Computer Modern serif font. Uppercase random variables. No equation number. Standalone equation. Any symbol, subscript, or notation visible is findable -- parity principle met. |
| Retrieval Value | "An RL update equation from a lecture" -- no method name, not self-contained. Would not surface for "one-step actor-critic" or "TD error advantage estimate" or "policy gradient with baseline." | "One-step actor-critic update using TD error as advantage with separate policy (theta) and value (w) parameters." Searchable but doesn't explain the variance reduction or the bridge from REINFORCE. | Natural prose identifying this as Sutton & Barto's one-step actor-critic update. G_t^{(1)} - v_hat(S_t,w) is the TD error delta_t used as advantage estimate, weighting the score function nabla log pi. Baseline v_hat reduces variance compared to REINFORCE (which uses full return). Enables online per-step policy updates. Separate parameters: theta (actor/policy) and w (critic/value). Foundation for A2C and A3C. Slide 62 of Princeton COS 598F, bridging REINFORCE to practical actor-critic methods. Domain vocabulary embedded (actor-critic, TD error, advantage, score function, baseline, variance reduction). Self-contained. Findable by "actor-critic update equation" or "one-step policy gradient with baseline." |
